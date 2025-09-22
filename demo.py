#!/usr/bin/env python

# Copyright (c) 2011 Bastian Venthur
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


"""Demo app for the AR.Drone.

This simple application allows to control the drone and see the drone's video
stream.
"""


import pygame
import signal
import sys

import libardrone

def signal_handler(sig, frame):
    """Handle Ctrl+C gracefully"""
    print("\nShutting down gracefully...")
    pygame.quit()
    sys.exit(0)

def main():
    # Set up signal handler for graceful shutdown
    signal.signal(signal.SIGINT, signal_handler)
    
    pygame.init()
    W, H = 640, 480
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("AR.Drone Demo - Connecting...")
    
    try:
        drone = libardrone.ARDrone()
    except Exception as e:
        print(f"Failed to initialize drone: {e}")
        pygame.quit()
        return
        
    clock = pygame.time.Clock()
    running = True
    connection_check_time = pygame.time.get_ticks()
    drone_connected = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
            elif event.type == pygame.KEYUP:
                drone.hover()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    drone.reset()
                    running = False
                # takeoff / land
                elif event.key == pygame.K_RETURN:
                    drone.takeoff()
                elif event.key == pygame.K_SPACE:
                    drone.land()
                # emergency
                elif event.key == pygame.K_BACKSPACE:
                    drone.reset()
                # forward / backward
                elif event.key == pygame.K_w:
                    drone.move_forward()
                elif event.key == pygame.K_s:
                    drone.move_backward()
                # left / right
                elif event.key == pygame.K_a:
                    drone.move_left()
                elif event.key == pygame.K_d:
                    drone.move_right()
                # up / down
                elif event.key == pygame.K_UP:
                    drone.move_up()
                elif event.key == pygame.K_DOWN:
                    drone.move_down()
                # turn left / turn right
                elif event.key == pygame.K_LEFT:
                    drone.turn_left()
                elif event.key == pygame.K_RIGHT:
                    drone.turn_right()
                # speed
                elif event.key == pygame.K_1:
                    drone.speed = 0.1
                elif event.key == pygame.K_2:
                    drone.speed = 0.2
                elif event.key == pygame.K_3:
                    drone.speed = 0.3
                elif event.key == pygame.K_4:
                    drone.speed = 0.4
                elif event.key == pygame.K_5:
                    drone.speed = 0.5
                elif event.key == pygame.K_6:
                    drone.speed = 0.6
                elif event.key == pygame.K_7:
                    drone.speed = 0.7
                elif event.key == pygame.K_8:
                    drone.speed = 0.8
                elif event.key == pygame.K_9:
                    drone.speed = 0.9
                elif event.key == pygame.K_0:
                    drone.speed = 1.0

        try:
            surface = pygame.image.fromstring(drone.image, (W, H), 'RGB')
            # battery status
            hud_color = (255, 0, 0) if drone.navdata.get('drone_state', dict()).get('emergency_mask', 1) else (10, 10, 255)
            bat = drone.navdata.get(0, dict()).get('battery', 0)
            f = pygame.font.Font(None, 20)
            hud = f.render('Battery: %i%%' % bat, True, hud_color)
            screen.blit(surface, (0, 0))
            screen.blit(hud, (10, 10))
            drone_connected = True
            pygame.display.set_caption("AR.Drone Demo - Connected")
        except:
            # No drone connected - show instructions or test pattern
            screen.fill((50, 50, 50))
            f = pygame.font.Font(None, 24)
            f_small = pygame.font.Font(None, 16)
            
            # Check if we should show test pattern (press T key)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_t]:
                # Show test pattern instead of instructions
                import time
                import math
                t = time.time()
                for y in range(H):
                    for x in range(W):
                        color_r = int(128 + 127 * math.sin(0.1 * x + t))
                        color_g = int(128 + 127 * math.sin(0.1 * y + t + 2))
                        color_b = int(128 + 127 * math.sin(0.1 * (x + y) + t + 4))
                        screen.set_at((x, y), (color_r, color_g, color_b))
                
                f = pygame.font.Font(None, 32)
                test_text = f.render("TEST PATTERN - Press T to toggle", True, (255, 255, 255))
                screen.blit(test_text, (W//2 - test_text.get_width()//2, H//2))
            else:
                # Check if we have any data from drone
                current_time = pygame.time.get_ticks()
                if current_time - connection_check_time > 3000:  # After 3 seconds
                    if not drone_connected and not drone.image and not drone.navdata:
                        title = f.render("No AR.Drone Connected", True, (255, 255, 255))
                        screen.blit(title, (W//2 - title.get_width()//2, 30))
                        
                        instructions = [
                            "Connect to AR.Drone WiFi network",
                            "Ensure drone IP is 192.168.1.1",
                            "",
                            "Controls (when connected):",
                            "RETURN - Takeoff (auto-resets emergency)",
                            "SPACE - Land", 
                            "BACKSPACE - Emergency Reset (if needed)",
                            "W/S - Forward/Backward",
                            "A/D - Left/Right",
                            "UP/DOWN - Altitude",
                            "LEFT/RIGHT - Turn",
                            "1-0 - Speed (0.1-1.0)",
                            "",
                            "T - Toggle test pattern (for video testing)",
                            "",
                            "Note: After landing, press RETURN to takeoff again",
                            "If takeoff fails, try BACKSPACE then RETURN",
                            "",
                            "ESC - Exit"
                        ]
                        
                        y_offset = 70
                        for line in instructions:
                            if line:
                                color = (255, 255, 0) if "Controls" in line else (200, 200, 200)
                                text = f_small.render(line, True, color)
                                screen.blit(text, (20, y_offset))
                            y_offset += 18
                        
                        # Add diagnostic information
                        diag_info = [
                            f"Image data: {'Available' if drone.image else 'None'}",
                            f"Nav data: {'Available' if drone.navdata else 'None'}",
                            f"Image size: {len(drone.image) if drone.image else 0} bytes"
                        ]
                        
                        y_offset += 20
                        for info in diag_info:
                            text = f_small.render(info, True, (100, 255, 100))
                            screen.blit(text, (20, y_offset))
                            y_offset += 16
                    else:
                        pygame.display.set_caption("AR.Drone Demo - No Video Signal")

        pygame.display.flip()
        clock.tick(50)
        pygame.display.set_caption("FPS: %.2f" % clock.get_fps())

    print("Shutting down...", end='')
    try:
        drone.halt()
        print("Ok.")
    except Exception as e:
        print(f"Error during shutdown: {e}")
    finally:
        pygame.quit()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted by user")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        pygame.quit()
