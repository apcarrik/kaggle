def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Coupon", "instances": 8147, "metric_value": 0.4734, "depth": 1}
	if obj[2]>1:
		# {"feature": "Coffeehouse", "instances": 5886, "metric_value": 0.4595, "depth": 2}
		if obj[8]<=1.0:
			# {"feature": "Distance", "instances": 3041, "metric_value": 0.4864, "depth": 3}
			if obj[11]<=2:
				# {"feature": "Passanger", "instances": 2734, "metric_value": 0.4834, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Restaurant20to50", "instances": 1643, "metric_value": 0.4939, "depth": 5}
					if obj[9]<=2.0:
						# {"feature": "Gender", "instances": 1593, "metric_value": 0.4963, "depth": 6}
						if obj[3]<=0:
							# {"feature": "Education", "instances": 803, "metric_value": 0.4917, "depth": 7}
							if obj[5]>1:
								# {"feature": "Age", "instances": 442, "metric_value": 0.4914, "depth": 8}
								if obj[4]>0:
									# {"feature": "Occupation", "instances": 364, "metric_value": 0.4929, "depth": 9}
									if obj[6]>1:
										# {"feature": "Time", "instances": 336, "metric_value": 0.4967, "depth": 10}
										if obj[1]<=3:
											# {"feature": "Bar", "instances": 277, "metric_value": 0.4939, "depth": 11}
											if obj[7]>-1.0:
												# {"feature": "Direction_same", "instances": 274, "metric_value": 0.4992, "depth": 12}
												if obj[10]<=0:
													return 'True'
												elif obj[10]>0:
													return 'True'
												else: return 'True'
											elif obj[7]<=-1.0:
												return 'False'
											else: return 'False'
										elif obj[1]>3:
											# {"feature": "Bar", "instances": 59, "metric_value": 0.4754, "depth": 11}
											if obj[7]>-1.0:
												# {"feature": "Direction_same", "instances": 56, "metric_value": 0.477, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[7]<=-1.0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[6]<=1:
										# {"feature": "Bar", "instances": 28, "metric_value": 0.381, "depth": 10}
										if obj[7]>-1.0:
											# {"feature": "Time", "instances": 24, "metric_value": 0.4048, "depth": 11}
											if obj[1]<=1:
												# {"feature": "Direction_same", "instances": 14, "metric_value": 0.2984, "depth": 12}
												if obj[10]>0:
													return 'True'
												elif obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[1]>1:
												# {"feature": "Direction_same", "instances": 10, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'True'
												elif obj[10]>0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[7]<=-1.0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[4]<=0:
									# {"feature": "Bar", "instances": 78, "metric_value": 0.3921, "depth": 9}
									if obj[7]<=1.0:
										# {"feature": "Occupation", "instances": 68, "metric_value": 0.3623, "depth": 10}
										if obj[6]<=8:
											# {"feature": "Time", "instances": 45, "metric_value": 0.2724, "depth": 11}
											if obj[1]<=1:
												# {"feature": "Direction_same", "instances": 27, "metric_value": 0.3691, "depth": 12}
												if obj[10]>0:
													return 'True'
												elif obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[1]>1:
												# {"feature": "Direction_same", "instances": 18, "metric_value": 0.0889, "depth": 12}
												if obj[10]<=0:
													return 'True'
												elif obj[10]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[6]>8:
											# {"feature": "Time", "instances": 23, "metric_value": 0.4783, "depth": 11}
											if obj[1]<=3:
												# {"feature": "Direction_same", "instances": 22, "metric_value": 0.4833, "depth": 12}
												if obj[10]>0:
													return 'True'
												elif obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[1]>3:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[7]>1.0:
										# {"feature": "Time", "instances": 10, "metric_value": 0.1778, "depth": 10}
										if obj[1]<=3:
											# {"feature": "Direction_same", "instances": 9, "metric_value": 0.1667, "depth": 11}
											if obj[10]>0:
												return 'False'
											elif obj[10]<=0:
												# {"feature": "Occupation", "instances": 4, "metric_value": 0.25, "depth": 12}
												if obj[6]<=6:
													return 'False'
												elif obj[6]>6:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[1]>3:
											return 'True'
										else: return 'True'
									else: return 'False'
								else: return 'True'
							elif obj[5]<=1:
								# {"feature": "Occupation", "instances": 361, "metric_value": 0.4732, "depth": 8}
								if obj[6]<=18:
									# {"feature": "Age", "instances": 327, "metric_value": 0.4854, "depth": 9}
									if obj[4]<=4:
										# {"feature": "Bar", "instances": 249, "metric_value": 0.491, "depth": 10}
										if obj[7]>0.0:
											# {"feature": "Time", "instances": 164, "metric_value": 0.4823, "depth": 11}
											if obj[1]<=2:
												# {"feature": "Direction_same", "instances": 118, "metric_value": 0.4747, "depth": 12}
												if obj[10]<=0:
													return 'True'
												elif obj[10]>0:
													return 'True'
												else: return 'True'
											elif obj[1]>2:
												# {"feature": "Direction_same", "instances": 46, "metric_value": 0.4988, "depth": 12}
												if obj[10]<=0:
													return 'False'
												elif obj[10]>0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[7]<=0.0:
											# {"feature": "Direction_same", "instances": 85, "metric_value": 0.4799, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Time", "instances": 63, "metric_value": 0.4736, "depth": 12}
												if obj[1]<=3:
													return 'False'
												elif obj[1]>3:
													return 'False'
												else: return 'False'
											elif obj[10]>0:
												# {"feature": "Time", "instances": 22, "metric_value": 0.4578, "depth": 12}
												if obj[1]<=1:
													return 'True'
												elif obj[1]>1:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[4]>4:
										# {"feature": "Time", "instances": 78, "metric_value": 0.4097, "depth": 10}
										if obj[1]<=1:
											# {"feature": "Bar", "instances": 48, "metric_value": 0.4822, "depth": 11}
											if obj[7]<=1.0:
												# {"feature": "Direction_same", "instances": 38, "metric_value": 0.4943, "depth": 12}
												if obj[10]>0:
													return 'True'
												elif obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[7]>1.0:
												# {"feature": "Direction_same", "instances": 10, "metric_value": 0.3429, "depth": 12}
												if obj[10]<=0:
													return 'True'
												elif obj[10]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[1]>1:
											# {"feature": "Bar", "instances": 30, "metric_value": 0.2716, "depth": 11}
											if obj[7]<=1.0:
												# {"feature": "Direction_same", "instances": 27, "metric_value": 0.3016, "depth": 12}
												if obj[10]<=0:
													return 'True'
												elif obj[10]>0:
													return 'True'
												else: return 'True'
											elif obj[7]>1.0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[6]>18:
									# {"feature": "Bar", "instances": 34, "metric_value": 0.2609, "depth": 9}
									if obj[7]>0.0:
										# {"feature": "Time", "instances": 23, "metric_value": 0.3734, "depth": 10}
										if obj[1]>0:
											# {"feature": "Direction_same", "instances": 16, "metric_value": 0.4227, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Age", "instances": 11, "metric_value": 0.3409, "depth": 12}
												if obj[4]>0:
													return 'True'
												elif obj[4]<=0:
													return 'True'
												else: return 'True'
											elif obj[10]>0:
												# {"feature": "Age", "instances": 5, "metric_value": 0.2667, "depth": 12}
												if obj[4]<=1:
													return 'False'
												elif obj[4]>1:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[1]<=0:
											# {"feature": "Direction_same", "instances": 7, "metric_value": 0.2143, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Age", "instances": 4, "metric_value": 0.3333, "depth": 12}
												if obj[4]>0:
													return 'True'
												elif obj[4]<=0:
													return 'True'
												else: return 'True'
											elif obj[10]>0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[7]<=0.0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[3]>0:
							# {"feature": "Bar", "instances": 790, "metric_value": 0.4942, "depth": 7}
							if obj[7]>-1.0:
								# {"feature": "Occupation", "instances": 782, "metric_value": 0.4958, "depth": 8}
								if obj[6]<=19:
									# {"feature": "Time", "instances": 723, "metric_value": 0.4956, "depth": 9}
									if obj[1]>0:
										# {"feature": "Age", "instances": 511, "metric_value": 0.4893, "depth": 10}
										if obj[4]<=6:
											# {"feature": "Education", "instances": 491, "metric_value": 0.4932, "depth": 11}
											if obj[5]>1:
												# {"feature": "Direction_same", "instances": 249, "metric_value": 0.4992, "depth": 12}
												if obj[10]<=0:
													return 'False'
												elif obj[10]>0:
													return 'True'
												else: return 'True'
											elif obj[5]<=1:
												# {"feature": "Direction_same", "instances": 242, "metric_value": 0.4831, "depth": 12}
												if obj[10]<=0:
													return 'True'
												elif obj[10]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[4]>6:
											# {"feature": "Education", "instances": 20, "metric_value": 0.2933, "depth": 11}
											if obj[5]<=2:
												# {"feature": "Direction_same", "instances": 15, "metric_value": 0.3852, "depth": 12}
												if obj[10]<=0:
													return 'True'
												elif obj[10]>0:
													return 'True'
												else: return 'True'
											elif obj[5]>2:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[1]<=0:
										# {"feature": "Direction_same", "instances": 212, "metric_value": 0.4927, "depth": 10}
										if obj[10]<=0:
											# {"feature": "Education", "instances": 111, "metric_value": 0.4731, "depth": 11}
											if obj[5]<=3:
												# {"feature": "Age", "instances": 101, "metric_value": 0.4753, "depth": 12}
												if obj[4]>1:
													return 'False'
												elif obj[4]<=1:
													return 'False'
												else: return 'False'
											elif obj[5]>3:
												# {"feature": "Age", "instances": 10, "metric_value": 0.3111, "depth": 12}
												if obj[4]<=6:
													return 'True'
												elif obj[4]>6:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[10]>0:
											# {"feature": "Education", "instances": 101, "metric_value": 0.474, "depth": 11}
											if obj[5]>0:
												# {"feature": "Age", "instances": 63, "metric_value": 0.4565, "depth": 12}
												if obj[4]<=3:
													return 'True'
												elif obj[4]>3:
													return 'True'
												else: return 'True'
											elif obj[5]<=0:
												# {"feature": "Age", "instances": 38, "metric_value": 0.4528, "depth": 12}
												if obj[4]<=3:
													return 'False'
												elif obj[4]>3:
													return 'True'
												else: return 'True'
											else: return 'False'
										else: return 'True'
									else: return 'False'
								elif obj[6]>19:
									# {"feature": "Education", "instances": 59, "metric_value": 0.4348, "depth": 9}
									if obj[5]<=2:
										# {"feature": "Time", "instances": 45, "metric_value": 0.4567, "depth": 10}
										if obj[1]<=2:
											# {"feature": "Age", "instances": 32, "metric_value": 0.4674, "depth": 11}
											if obj[4]<=3:
												# {"feature": "Direction_same", "instances": 23, "metric_value": 0.4328, "depth": 12}
												if obj[10]>0:
													return 'True'
												elif obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[4]>3:
												# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4444, "depth": 12}
												if obj[10]>0:
													return 'False'
												elif obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[1]>2:
											# {"feature": "Direction_same", "instances": 13, "metric_value": 0.3192, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Age", "instances": 8, "metric_value": 0.0, "depth": 12}
												if obj[4]>1:
													return 'False'
												elif obj[4]<=1:
													return 'True'
												else: return 'True'
											elif obj[10]>0:
												# {"feature": "Age", "instances": 5, "metric_value": 0.0, "depth": 12}
												if obj[4]<=1:
													return 'False'
												elif obj[4]>1:
													return 'True'
												else: return 'True'
											else: return 'False'
										else: return 'False'
									elif obj[5]>2:
										# {"feature": "Age", "instances": 14, "metric_value": 0.1714, "depth": 10}
										if obj[4]<=1:
											return 'False'
										elif obj[4]>1:
											# {"feature": "Time", "instances": 5, "metric_value": 0.3, "depth": 11}
											if obj[1]>0:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.25, "depth": 12}
												if obj[10]>0:
													return 'False'
												elif obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[1]<=0:
												return 'True'
											else: return 'True'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[7]<=-1.0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[9]>2.0:
						# {"feature": "Time", "instances": 50, "metric_value": 0.3467, "depth": 6}
						if obj[1]>0:
							# {"feature": "Occupation", "instances": 39, "metric_value": 0.404, "depth": 7}
							if obj[6]<=9:
								# {"feature": "Age", "instances": 33, "metric_value": 0.3827, "depth": 8}
								if obj[4]>0:
									# {"feature": "Direction_same", "instances": 25, "metric_value": 0.416, "depth": 9}
									if obj[10]<=0:
										# {"feature": "Gender", "instances": 15, "metric_value": 0.4741, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Education", "instances": 9, "metric_value": 0.4938, "depth": 11}
											if obj[5]<=4:
												# {"feature": "Bar", "instances": 9, "metric_value": 0.4938, "depth": 12}
												if obj[7]<=0.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]>0:
											# {"feature": "Education", "instances": 6, "metric_value": 0.4444, "depth": 11}
											if obj[5]>1:
												# {"feature": "Bar", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[7]<=2.0:
													return 'True'
												else: return 'True'
											elif obj[5]<=1:
												# {"feature": "Bar", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[7]<=2.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[10]>0:
										# {"feature": "Gender", "instances": 10, "metric_value": 0.1778, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Education", "instances": 9, "metric_value": 0.1778, "depth": 11}
											if obj[5]>3:
												# {"feature": "Bar", "instances": 5, "metric_value": 0.32, "depth": 12}
												if obj[7]<=0.0:
													return 'True'
												else: return 'True'
											elif obj[5]<=3:
												return 'True'
											else: return 'True'
										elif obj[3]>0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[4]<=0:
									# {"feature": "Direction_same", "instances": 8, "metric_value": 0.1667, "depth": 9}
									if obj[10]<=0:
										return 'True'
									elif obj[10]>0:
										# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[3]<=1:
											# {"feature": "Education", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Bar", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[7]<=1.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[6]>9:
								# {"feature": "Gender", "instances": 6, "metric_value": 0.0, "depth": 8}
								if obj[3]<=0:
									return 'False'
								elif obj[3]>0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[1]<=0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[0]>1:
					# {"feature": "Education", "instances": 1091, "metric_value": 0.461, "depth": 5}
					if obj[5]>1:
						# {"feature": "Time", "instances": 569, "metric_value": 0.4738, "depth": 6}
						if obj[1]>0:
							# {"feature": "Restaurant20to50", "instances": 439, "metric_value": 0.486, "depth": 7}
							if obj[9]>0.0:
								# {"feature": "Age", "instances": 331, "metric_value": 0.493, "depth": 8}
								if obj[4]<=5:
									# {"feature": "Occupation", "instances": 271, "metric_value": 0.4881, "depth": 9}
									if obj[6]>1:
										# {"feature": "Bar", "instances": 246, "metric_value": 0.4952, "depth": 10}
										if obj[7]<=1.0:
											# {"feature": "Gender", "instances": 170, "metric_value": 0.4919, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 86, "metric_value": 0.4976, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 84, "metric_value": 0.4861, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[7]>1.0:
											# {"feature": "Gender", "instances": 76, "metric_value": 0.4997, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 41, "metric_value": 0.4997, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 35, "metric_value": 0.4996, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[6]<=1:
										# {"feature": "Bar", "instances": 25, "metric_value": 0.3947, "depth": 10}
										if obj[7]>0.0:
											# {"feature": "Gender", "instances": 15, "metric_value": 0.4405, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 8, "metric_value": 0.4688, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4082, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[7]<=0.0:
											# {"feature": "Gender", "instances": 10, "metric_value": 0.3, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 8, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[4]>5:
									# {"feature": "Occupation", "instances": 60, "metric_value": 0.4415, "depth": 9}
									if obj[6]<=19:
										# {"feature": "Gender", "instances": 53, "metric_value": 0.4913, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Bar", "instances": 30, "metric_value": 0.4833, "depth": 11}
											if obj[7]>0.0:
												# {"feature": "Direction_same", "instances": 16, "metric_value": 0.4688, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[7]<=0.0:
												# {"feature": "Direction_same", "instances": 14, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]>0:
											# {"feature": "Bar", "instances": 23, "metric_value": 0.4915, "depth": 11}
											if obj[7]>0.0:
												# {"feature": "Direction_same", "instances": 16, "metric_value": 0.4922, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[7]<=0.0:
												# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4898, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[6]>19:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[9]<=0.0:
								# {"feature": "Bar", "instances": 108, "metric_value": 0.4265, "depth": 8}
								if obj[7]<=1.0:
									# {"feature": "Occupation", "instances": 98, "metric_value": 0.4579, "depth": 9}
									if obj[6]<=20:
										# {"feature": "Age", "instances": 94, "metric_value": 0.462, "depth": 10}
										if obj[4]<=2:
											# {"feature": "Gender", "instances": 56, "metric_value": 0.426, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 28, "metric_value": 0.477, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 28, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[4]>2:
											# {"feature": "Gender", "instances": 38, "metric_value": 0.4985, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 25, "metric_value": 0.4992, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 13, "metric_value": 0.497, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[6]>20:
										return 'True'
									else: return 'True'
								elif obj[7]>1.0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[1]<=0:
							# {"feature": "Occupation", "instances": 130, "metric_value": 0.3967, "depth": 7}
							if obj[6]<=6:
								# {"feature": "Age", "instances": 65, "metric_value": 0.3082, "depth": 8}
								if obj[4]<=6:
									# {"feature": "Restaurant20to50", "instances": 61, "metric_value": 0.2842, "depth": 9}
									if obj[9]>0.0:
										# {"feature": "Bar", "instances": 44, "metric_value": 0.3463, "depth": 10}
										if obj[7]<=2.0:
											# {"feature": "Gender", "instances": 42, "metric_value": 0.3585, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 25, "metric_value": 0.32, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 17, "metric_value": 0.4152, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[7]>2.0:
											return 'True'
										else: return 'True'
									elif obj[9]<=0.0:
										# {"feature": "Bar", "instances": 17, "metric_value": 0.1029, "depth": 10}
										if obj[7]<=0.0:
											return 'True'
										elif obj[7]>0.0:
											# {"feature": "Gender", "instances": 8, "metric_value": 0.1875, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[4]>6:
									# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.3333, "depth": 9}
									if obj[9]<=0.0:
										# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[3]<=1:
											# {"feature": "Bar", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[7]<=0.0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[9]>0.0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[6]>6:
								# {"feature": "Age", "instances": 65, "metric_value": 0.4572, "depth": 8}
								if obj[4]<=6:
									# {"feature": "Gender", "instances": 59, "metric_value": 0.4525, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Bar", "instances": 32, "metric_value": 0.4718, "depth": 10}
										if obj[7]<=3.0:
											# {"feature": "Restaurant20to50", "instances": 31, "metric_value": 0.4753, "depth": 11}
											if obj[9]<=2.0:
												# {"feature": "Direction_same", "instances": 30, "metric_value": 0.4911, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[9]>2.0:
												return 'True'
											else: return 'True'
										elif obj[7]>3.0:
											return 'True'
										else: return 'True'
									elif obj[3]>0:
										# {"feature": "Restaurant20to50", "instances": 27, "metric_value": 0.3771, "depth": 10}
										if obj[9]>0.0:
											# {"feature": "Bar", "instances": 22, "metric_value": 0.4463, "depth": 11}
											if obj[7]>0.0:
												# {"feature": "Direction_same", "instances": 11, "metric_value": 0.3967, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[7]<=0.0:
												# {"feature": "Direction_same", "instances": 11, "metric_value": 0.4959, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[9]<=0.0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[4]>6:
									# {"feature": "Bar", "instances": 6, "metric_value": 0.4, "depth": 9}
									if obj[7]<=1.0:
										# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.3, "depth": 10}
										if obj[9]<=0.0:
											# {"feature": "Gender", "instances": 4, "metric_value": 0.375, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[9]>0.0:
											return 'True'
										else: return 'True'
									elif obj[7]>1.0:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					elif obj[5]<=1:
						# {"feature": "Bar", "instances": 522, "metric_value": 0.4308, "depth": 6}
						if obj[7]<=0.0:
							# {"feature": "Time", "instances": 283, "metric_value": 0.453, "depth": 7}
							if obj[1]<=2:
								# {"feature": "Gender", "instances": 163, "metric_value": 0.4818, "depth": 8}
								if obj[3]>0:
									# {"feature": "Occupation", "instances": 112, "metric_value": 0.4703, "depth": 9}
									if obj[6]<=12:
										# {"feature": "Age", "instances": 97, "metric_value": 0.483, "depth": 10}
										if obj[4]>0:
											# {"feature": "Restaurant20to50", "instances": 85, "metric_value": 0.4902, "depth": 11}
											if obj[9]<=1.0:
												# {"feature": "Direction_same", "instances": 70, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[9]>1.0:
												# {"feature": "Direction_same", "instances": 15, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[4]<=0:
											# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.3125, "depth": 11}
											if obj[9]<=0.0:
												# {"feature": "Direction_same", "instances": 8, "metric_value": 0.2188, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[9]>0.0:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[6]>12:
										# {"feature": "Age", "instances": 15, "metric_value": 0.3143, "depth": 10}
										if obj[4]>1:
											# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.3367, "depth": 11}
											if obj[9]<=1.0:
												# {"feature": "Direction_same", "instances": 14, "metric_value": 0.3367, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[4]<=1:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[3]<=0:
									# {"feature": "Restaurant20to50", "instances": 51, "metric_value": 0.4549, "depth": 9}
									if obj[9]<=1.0:
										# {"feature": "Occupation", "instances": 47, "metric_value": 0.4177, "depth": 10}
										if obj[6]<=11:
											# {"feature": "Age", "instances": 38, "metric_value": 0.3916, "depth": 11}
											if obj[4]>0:
												# {"feature": "Direction_same", "instances": 34, "metric_value": 0.4377, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[4]<=0:
												return 'False'
											else: return 'False'
										elif obj[6]>11:
											# {"feature": "Age", "instances": 9, "metric_value": 0.3333, "depth": 11}
											if obj[4]<=3:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[4]>3:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[9]>1.0:
										# {"feature": "Age", "instances": 4, "metric_value": 0.0, "depth": 10}
										if obj[4]<=0:
											return 'True'
										elif obj[4]>0:
											return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'False'
							elif obj[1]>2:
								# {"feature": "Restaurant20to50", "instances": 120, "metric_value": 0.3772, "depth": 8}
								if obj[9]<=1.0:
									# {"feature": "Occupation", "instances": 98, "metric_value": 0.4058, "depth": 9}
									if obj[6]>1:
										# {"feature": "Age", "instances": 71, "metric_value": 0.4479, "depth": 10}
										if obj[4]>2:
											# {"feature": "Gender", "instances": 44, "metric_value": 0.4161, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 23, "metric_value": 0.4234, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 21, "metric_value": 0.4082, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[4]<=2:
											# {"feature": "Gender", "instances": 27, "metric_value": 0.4938, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 18, "metric_value": 0.4938, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4938, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[6]<=1:
										# {"feature": "Age", "instances": 27, "metric_value": 0.2311, "depth": 10}
										if obj[4]>2:
											# {"feature": "Gender", "instances": 16, "metric_value": 0.1111, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 9, "metric_value": 0.1975, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												return 'True'
											else: return 'True'
										elif obj[4]<=2:
											# {"feature": "Gender", "instances": 11, "metric_value": 0.3818, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 10, "metric_value": 0.42, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[9]>1.0:
									# {"feature": "Age", "instances": 22, "metric_value": 0.1455, "depth": 9}
									if obj[4]<=2:
										return 'True'
									elif obj[4]>2:
										# {"feature": "Gender", "instances": 10, "metric_value": 0.3048, "depth": 10}
										if obj[3]>0:
											# {"feature": "Occupation", "instances": 7, "metric_value": 0.2143, "depth": 11}
											if obj[6]<=1:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[6]>1:
												return 'True'
											else: return 'True'
										elif obj[3]<=0:
											# {"feature": "Occupation", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[6]<=7:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[7]>0.0:
							# {"feature": "Age", "instances": 239, "metric_value": 0.372, "depth": 7}
							if obj[4]<=3:
								# {"feature": "Restaurant20to50", "instances": 154, "metric_value": 0.3166, "depth": 8}
								if obj[9]>-1.0:
									# {"feature": "Occupation", "instances": 147, "metric_value": 0.3001, "depth": 9}
									if obj[6]<=17:
										# {"feature": "Time", "instances": 132, "metric_value": 0.3319, "depth": 10}
										if obj[1]<=3:
											# {"feature": "Gender", "instances": 90, "metric_value": 0.3049, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 49, "metric_value": 0.2732, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 41, "metric_value": 0.3427, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[1]>3:
											# {"feature": "Gender", "instances": 42, "metric_value": 0.373, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 24, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 18, "metric_value": 0.2778, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[6]>17:
										return 'True'
									else: return 'True'
								elif obj[9]<=-1.0:
									# {"feature": "Time", "instances": 7, "metric_value": 0.4048, "depth": 9}
									if obj[1]<=2:
										# {"feature": "Gender", "instances": 4, "metric_value": 0.375, "depth": 10}
										if obj[3]<=1:
											# {"feature": "Occupation", "instances": 4, "metric_value": 0.375, "depth": 11}
											if obj[6]<=5:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[1]>2:
										# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[3]<=1:
											# {"feature": "Occupation", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[6]<=5:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[4]>3:
								# {"feature": "Time", "instances": 85, "metric_value": 0.4298, "depth": 8}
								if obj[1]<=3:
									# {"feature": "Occupation", "instances": 66, "metric_value": 0.4084, "depth": 9}
									if obj[6]>5:
										# {"feature": "Gender", "instances": 38, "metric_value": 0.3811, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Restaurant20to50", "instances": 30, "metric_value": 0.3576, "depth": 11}
											if obj[9]>0.0:
												# {"feature": "Direction_same", "instances": 22, "metric_value": 0.3512, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[9]<=0.0:
												# {"feature": "Direction_same", "instances": 8, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]>0:
											# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.4667, "depth": 11}
											if obj[9]>1.0:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[9]<=1.0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[6]<=5:
										# {"feature": "Gender", "instances": 28, "metric_value": 0.4232, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Restaurant20to50", "instances": 22, "metric_value": 0.4211, "depth": 11}
											if obj[9]<=1.0:
												# {"feature": "Direction_same", "instances": 19, "metric_value": 0.4875, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[9]>1.0:
												return 'True'
											else: return 'True'
										elif obj[3]>0:
											# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.0, "depth": 11}
											if obj[9]<=1.0:
												return 'True'
											elif obj[9]>1.0:
												return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'True'
								elif obj[1]>3:
									# {"feature": "Restaurant20to50", "instances": 19, "metric_value": 0.4145, "depth": 9}
									if obj[9]>0.0:
										# {"feature": "Occupation", "instances": 16, "metric_value": 0.4872, "depth": 10}
										if obj[6]>1:
											# {"feature": "Gender", "instances": 13, "metric_value": 0.4965, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 11, "metric_value": 0.4959, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[6]<=1:
											# {"feature": "Gender", "instances": 3, "metric_value": 0.3333, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[3]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[9]<=0.0:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[11]>2:
				# {"feature": "Time", "instances": 307, "metric_value": 0.454, "depth": 4}
				if obj[1]>0:
					# {"feature": "Education", "instances": 255, "metric_value": 0.4745, "depth": 5}
					if obj[5]<=2:
						# {"feature": "Bar", "instances": 207, "metric_value": 0.4639, "depth": 6}
						if obj[7]<=0.0:
							# {"feature": "Age", "instances": 109, "metric_value": 0.4815, "depth": 7}
							if obj[4]<=5:
								# {"feature": "Occupation", "instances": 88, "metric_value": 0.4863, "depth": 8}
								if obj[6]<=22:
									# {"feature": "Gender", "instances": 86, "metric_value": 0.4897, "depth": 9}
									if obj[3]>0:
										# {"feature": "Restaurant20to50", "instances": 48, "metric_value": 0.4977, "depth": 10}
										if obj[9]<=1.0:
											# {"feature": "Passanger", "instances": 43, "metric_value": 0.4997, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 43, "metric_value": 0.4997, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[9]>1.0:
											# {"feature": "Passanger", "instances": 5, "metric_value": 0.48, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[3]<=0:
										# {"feature": "Restaurant20to50", "instances": 38, "metric_value": 0.439, "depth": 10}
										if obj[9]>0.0:
											# {"feature": "Passanger", "instances": 30, "metric_value": 0.4978, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 30, "metric_value": 0.4978, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[9]<=0.0:
											# {"feature": "Passanger", "instances": 8, "metric_value": 0.2188, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 8, "metric_value": 0.2188, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[6]>22:
									return 'False'
								else: return 'False'
							elif obj[4]>5:
								# {"feature": "Occupation", "instances": 21, "metric_value": 0.2245, "depth": 8}
								if obj[6]<=9:
									# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.1071, "depth": 9}
									if obj[9]<=1.0:
										return 'False'
									elif obj[9]>1.0:
										# {"feature": "Gender", "instances": 4, "metric_value": 0.25, "depth": 10}
										if obj[3]>0:
											return 'False'
										elif obj[3]<=0:
											# {"feature": "Passanger", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[6]>9:
									# {"feature": "Gender", "instances": 7, "metric_value": 0.1905, "depth": 9}
									if obj[3]<=0:
										return 'True'
									elif obj[3]>0:
										# {"feature": "Passanger", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[9]<=1.0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'False'
						elif obj[7]>0.0:
							# {"feature": "Occupation", "instances": 98, "metric_value": 0.3936, "depth": 7}
							if obj[6]>1:
								# {"feature": "Age", "instances": 83, "metric_value": 0.3527, "depth": 8}
								if obj[4]<=3:
									# {"feature": "Restaurant20to50", "instances": 46, "metric_value": 0.2536, "depth": 9}
									if obj[9]>0.0:
										# {"feature": "Gender", "instances": 42, "metric_value": 0.2731, "depth": 10}
										if obj[3]>0:
											# {"feature": "Passanger", "instances": 24, "metric_value": 0.2188, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 24, "metric_value": 0.2188, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[3]<=0:
											# {"feature": "Passanger", "instances": 18, "metric_value": 0.3457, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 18, "metric_value": 0.3457, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[9]<=0.0:
										return 'False'
									else: return 'False'
								elif obj[4]>3:
									# {"feature": "Restaurant20to50", "instances": 37, "metric_value": 0.434, "depth": 9}
									if obj[9]<=1.0:
										# {"feature": "Gender", "instances": 27, "metric_value": 0.4118, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Passanger", "instances": 19, "metric_value": 0.3878, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 19, "metric_value": 0.3878, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[3]>0:
											# {"feature": "Passanger", "instances": 8, "metric_value": 0.4688, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 8, "metric_value": 0.4688, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[9]>1.0:
										# {"feature": "Gender", "instances": 10, "metric_value": 0.475, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Passanger", "instances": 8, "metric_value": 0.4688, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 8, "metric_value": 0.4688, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]>0:
											# {"feature": "Passanger", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'False'
							elif obj[6]<=1:
								# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.4286, "depth": 8}
								if obj[9]>0.0:
									# {"feature": "Gender", "instances": 14, "metric_value": 0.3937, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Age", "instances": 9, "metric_value": 0.2963, "depth": 10}
										if obj[4]<=1:
											# {"feature": "Passanger", "instances": 6, "metric_value": 0.4444, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[4]>1:
											return 'True'
										else: return 'True'
									elif obj[3]>0:
										# {"feature": "Age", "instances": 5, "metric_value": 0.2667, "depth": 10}
										if obj[4]<=1:
											# {"feature": "Passanger", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[4]>1:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[9]<=0.0:
									return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'False'
					elif obj[5]>2:
						# {"feature": "Occupation", "instances": 48, "metric_value": 0.407, "depth": 6}
						if obj[6]>4:
							# {"feature": "Age", "instances": 29, "metric_value": 0.4708, "depth": 7}
							if obj[4]<=3:
								# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.4167, "depth": 8}
								if obj[9]>-1.0:
									# {"feature": "Bar", "instances": 15, "metric_value": 0.4074, "depth": 9}
									if obj[7]>0.0:
										# {"feature": "Gender", "instances": 9, "metric_value": 0.4815, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Passanger", "instances": 6, "metric_value": 0.5, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]>0:
											# {"feature": "Passanger", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[7]<=0.0:
										# {"feature": "Gender", "instances": 6, "metric_value": 0.25, "depth": 10}
										if obj[3]>0:
											# {"feature": "Passanger", "instances": 4, "metric_value": 0.375, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[9]<=-1.0:
									return 'False'
								else: return 'False'
							elif obj[4]>3:
								# {"feature": "Bar", "instances": 13, "metric_value": 0.3547, "depth": 8}
								if obj[7]<=0.0:
									# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.2963, "depth": 9}
									if obj[9]>1.0:
										# {"feature": "Passanger", "instances": 6, "metric_value": 0.4444, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Gender", "instances": 6, "metric_value": 0.4444, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[9]<=1.0:
										return 'False'
									else: return 'False'
								elif obj[7]>0.0:
									# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.25, "depth": 9}
									if obj[9]<=0.0:
										return 'True'
									elif obj[9]>0.0:
										# {"feature": "Gender", "instances": 2, "metric_value": 0.0, "depth": 10}
										if obj[3]>0:
											return 'True'
										elif obj[3]<=0:
											return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[6]<=4:
							# {"feature": "Age", "instances": 19, "metric_value": 0.2241, "depth": 7}
							if obj[4]>1:
								# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.127, "depth": 8}
								if obj[9]>0.0:
									# {"feature": "Bar", "instances": 9, "metric_value": 0.1778, "depth": 9}
									if obj[7]<=0.0:
										# {"feature": "Gender", "instances": 5, "metric_value": 0.3, "depth": 10}
										if obj[3]>0:
											# {"feature": "Passanger", "instances": 4, "metric_value": 0.375, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]>0.0:
										return 'True'
									else: return 'True'
								elif obj[9]<=0.0:
									return 'True'
								else: return 'True'
							elif obj[4]<=1:
								# {"feature": "Gender", "instances": 5, "metric_value": 0.2667, "depth": 8}
								if obj[3]>0:
									# {"feature": "Passanger", "instances": 3, "metric_value": 0.4444, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Bar", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[7]<=1.0:
											# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[9]<=0.0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[3]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[1]<=0:
					# {"feature": "Passanger", "instances": 52, "metric_value": 0.1399, "depth": 5}
					if obj[0]>0:
						# {"feature": "Age", "instances": 46, "metric_value": 0.1098, "depth": 6}
						if obj[4]>1:
							return 'False'
						elif obj[4]<=1:
							# {"feature": "Occupation", "instances": 19, "metric_value": 0.2241, "depth": 7}
							if obj[6]>1:
								# {"feature": "Education", "instances": 14, "metric_value": 0.0952, "depth": 8}
								if obj[5]>0:
									return 'False'
								elif obj[5]<=0:
									# {"feature": "Bar", "instances": 3, "metric_value": 0.0, "depth": 9}
									if obj[7]>0.0:
										return 'False'
									elif obj[7]<=0.0:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[6]<=1:
								# {"feature": "Education", "instances": 5, "metric_value": 0.4, "depth": 8}
								if obj[5]>0:
									# {"feature": "Bar", "instances": 4, "metric_value": 0.3333, "depth": 9}
									if obj[7]>0.0:
										# {"feature": "Gender", "instances": 3, "metric_value": 0.3333, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[9]<=1.0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]>0:
											return 'False'
										else: return 'False'
									elif obj[7]<=0.0:
										return 'True'
									else: return 'True'
								elif obj[5]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[0]<=0:
						# {"feature": "Age", "instances": 6, "metric_value": 0.0, "depth": 6}
						if obj[4]<=5:
							return 'True'
						elif obj[4]>5:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		elif obj[8]>1.0:
			# {"feature": "Distance", "instances": 2845, "metric_value": 0.4173, "depth": 3}
			if obj[11]<=2:
				# {"feature": "Passanger", "instances": 2564, "metric_value": 0.4036, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Occupation", "instances": 1682, "metric_value": 0.433, "depth": 5}
					if obj[6]<=18.296160208955353:
						# {"feature": "Age", "instances": 1558, "metric_value": 0.4406, "depth": 6}
						if obj[4]>0:
							# {"feature": "Bar", "instances": 1347, "metric_value": 0.4317, "depth": 7}
							if obj[7]>0.0:
								# {"feature": "Time", "instances": 943, "metric_value": 0.4423, "depth": 8}
								if obj[1]<=3:
									# {"feature": "Restaurant20to50", "instances": 775, "metric_value": 0.4532, "depth": 9}
									if obj[9]<=1.0:
										# {"feature": "Education", "instances": 424, "metric_value": 0.4706, "depth": 10}
										if obj[5]>1:
											# {"feature": "Gender", "instances": 269, "metric_value": 0.4591, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 145, "metric_value": 0.4421, "depth": 12}
												if obj[10]<=0:
													return 'True'
												elif obj[10]>0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 124, "metric_value": 0.475, "depth": 12}
												if obj[10]<=0:
													return 'True'
												elif obj[10]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[5]<=1:
											# {"feature": "Direction_same", "instances": 155, "metric_value": 0.4809, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Gender", "instances": 78, "metric_value": 0.494, "depth": 12}
												if obj[3]>0:
													return 'True'
												elif obj[3]<=0:
													return 'False'
												else: return 'False'
											elif obj[10]>0:
												# {"feature": "Gender", "instances": 77, "metric_value": 0.4625, "depth": 12}
												if obj[3]<=0:
													return 'True'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[9]>1.0:
										# {"feature": "Education", "instances": 351, "metric_value": 0.4271, "depth": 10}
										if obj[5]>0:
											# {"feature": "Direction_same", "instances": 268, "metric_value": 0.437, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Gender", "instances": 149, "metric_value": 0.4711, "depth": 12}
												if obj[3]<=0:
													return 'True'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											elif obj[10]>0:
												# {"feature": "Gender", "instances": 119, "metric_value": 0.3842, "depth": 12}
												if obj[3]<=0:
													return 'True'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[5]<=0:
											# {"feature": "Direction_same", "instances": 83, "metric_value": 0.3607, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Gender", "instances": 50, "metric_value": 0.3168, "depth": 12}
												if obj[3]<=0:
													return 'True'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											elif obj[10]>0:
												# {"feature": "Gender", "instances": 33, "metric_value": 0.4222, "depth": 12}
												if obj[3]>0:
													return 'True'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[1]>3:
									# {"feature": "Restaurant20to50", "instances": 168, "metric_value": 0.378, "depth": 9}
									if obj[9]<=3.0:
										# {"feature": "Education", "instances": 164, "metric_value": 0.3734, "depth": 10}
										if obj[5]<=3:
											# {"feature": "Gender", "instances": 156, "metric_value": 0.3806, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 80, "metric_value": 0.3622, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 76, "metric_value": 0.3999, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[5]>3:
											# {"feature": "Gender", "instances": 8, "metric_value": 0.2083, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 0.2778, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[9]>3.0:
										# {"feature": "Education", "instances": 4, "metric_value": 0.3333, "depth": 10}
										if obj[5]>1:
											# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[5]<=1:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[7]<=0.0:
								# {"feature": "Time", "instances": 404, "metric_value": 0.3985, "depth": 8}
								if obj[1]<=2:
									# {"feature": "Restaurant20to50", "instances": 282, "metric_value": 0.3784, "depth": 9}
									if obj[9]>-1.0:
										# {"feature": "Gender", "instances": 278, "metric_value": 0.3819, "depth": 10}
										if obj[3]>0:
											# {"feature": "Education", "instances": 181, "metric_value": 0.4021, "depth": 11}
											if obj[5]<=2:
												# {"feature": "Direction_same", "instances": 141, "metric_value": 0.387, "depth": 12}
												if obj[10]<=0:
													return 'True'
												elif obj[10]>0:
													return 'True'
												else: return 'True'
											elif obj[5]>2:
												# {"feature": "Direction_same", "instances": 40, "metric_value": 0.4547, "depth": 12}
												if obj[10]<=0:
													return 'True'
												elif obj[10]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]<=0:
											# {"feature": "Direction_same", "instances": 97, "metric_value": 0.3348, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Education", "instances": 59, "metric_value": 0.3747, "depth": 12}
												if obj[5]<=3:
													return 'True'
												elif obj[5]>3:
													return 'True'
												else: return 'True'
											elif obj[10]>0:
												# {"feature": "Education", "instances": 38, "metric_value": 0.2469, "depth": 12}
												if obj[5]<=1:
													return 'True'
												elif obj[5]>1:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[9]<=-1.0:
										return 'True'
									else: return 'True'
								elif obj[1]>2:
									# {"feature": "Gender", "instances": 122, "metric_value": 0.438, "depth": 9}
									if obj[3]>0:
										# {"feature": "Restaurant20to50", "instances": 82, "metric_value": 0.4411, "depth": 10}
										if obj[9]>0.0:
											# {"feature": "Education", "instances": 78, "metric_value": 0.443, "depth": 11}
											if obj[5]>0:
												# {"feature": "Direction_same", "instances": 51, "metric_value": 0.4281, "depth": 12}
												if obj[10]<=0:
													return 'True'
												elif obj[10]>0:
													return 'True'
												else: return 'True'
											elif obj[5]<=0:
												# {"feature": "Direction_same", "instances": 27, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'True'
												elif obj[10]>0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[9]<=0.0:
											# {"feature": "Education", "instances": 4, "metric_value": 0.0, "depth": 11}
											if obj[5]<=2:
												return 'False'
											elif obj[5]>2:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[3]<=0:
										# {"feature": "Restaurant20to50", "instances": 40, "metric_value": 0.3832, "depth": 10}
										if obj[9]>0.0:
											# {"feature": "Direction_same", "instances": 31, "metric_value": 0.4249, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Education", "instances": 22, "metric_value": 0.347, "depth": 12}
												if obj[5]>0:
													return 'True'
												elif obj[5]<=0:
													return 'True'
												else: return 'True'
											elif obj[10]>0:
												# {"feature": "Education", "instances": 9, "metric_value": 0.4815, "depth": 12}
												if obj[5]<=0:
													return 'True'
												elif obj[5]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[9]<=0.0:
											# {"feature": "Direction_same", "instances": 9, "metric_value": 0.1905, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Education", "instances": 7, "metric_value": 0.2449, "depth": 12}
												if obj[5]<=0:
													return 'True'
												else: return 'True'
											elif obj[10]>0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[4]<=0:
							# {"feature": "Education", "instances": 211, "metric_value": 0.465, "depth": 7}
							if obj[5]<=3:
								# {"feature": "Restaurant20to50", "instances": 180, "metric_value": 0.477, "depth": 8}
								if obj[9]<=2.0:
									# {"feature": "Bar", "instances": 143, "metric_value": 0.4689, "depth": 9}
									if obj[7]<=3.0:
										# {"feature": "Gender", "instances": 136, "metric_value": 0.4722, "depth": 10}
										if obj[3]>0:
											# {"feature": "Time", "instances": 98, "metric_value": 0.4671, "depth": 11}
											if obj[1]<=2:
												# {"feature": "Direction_same", "instances": 63, "metric_value": 0.454, "depth": 12}
												if obj[10]>0:
													return 'True'
												elif obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[1]>2:
												# {"feature": "Direction_same", "instances": 35, "metric_value": 0.4898, "depth": 12}
												if obj[10]<=0:
													return 'True'
												elif obj[10]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]<=0:
											# {"feature": "Time", "instances": 38, "metric_value": 0.4499, "depth": 11}
											if obj[1]>0:
												# {"feature": "Direction_same", "instances": 25, "metric_value": 0.492, "depth": 12}
												if obj[10]<=0:
													return 'False'
												elif obj[10]>0:
													return 'True'
												else: return 'True'
											elif obj[1]<=0:
												# {"feature": "Direction_same", "instances": 13, "metric_value": 0.2308, "depth": 12}
												if obj[10]<=0:
													return 'False'
												elif obj[10]>0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[7]>3.0:
										return 'True'
									else: return 'True'
								elif obj[9]>2.0:
									# {"feature": "Gender", "instances": 37, "metric_value": 0.3338, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Time", "instances": 21, "metric_value": 0.4233, "depth": 10}
										if obj[1]<=3:
											# {"feature": "Direction_same", "instances": 18, "metric_value": 0.4333, "depth": 11}
											if obj[10]>0:
												# {"feature": "Bar", "instances": 10, "metric_value": 0.4444, "depth": 12}
												if obj[7]>1.0:
													return 'True'
												elif obj[7]<=1.0:
													return 'True'
												else: return 'True'
											elif obj[10]<=0:
												# {"feature": "Bar", "instances": 8, "metric_value": 0.25, "depth": 12}
												if obj[7]>1.0:
													return 'False'
												elif obj[7]<=1.0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[1]>3:
											return 'True'
										else: return 'True'
									elif obj[3]>0:
										# {"feature": "Time", "instances": 16, "metric_value": 0.1042, "depth": 10}
										if obj[1]<=1:
											return 'False'
										elif obj[1]>1:
											# {"feature": "Bar", "instances": 6, "metric_value": 0.2222, "depth": 11}
											if obj[7]<=2.0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[7]>2.0:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[5]>3:
								# {"feature": "Time", "instances": 31, "metric_value": 0.2525, "depth": 8}
								if obj[1]<=3:
									# {"feature": "Gender", "instances": 23, "metric_value": 0.323, "depth": 9}
									if obj[3]>0:
										# {"feature": "Bar", "instances": 14, "metric_value": 0.2041, "depth": 10}
										if obj[7]>0.0:
											# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4048, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[9]<=1.0:
													return 'True'
												else: return 'True'
											elif obj[10]>0:
												# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[9]<=1.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[7]<=0.0:
											return 'True'
										else: return 'True'
									elif obj[3]<=0:
										# {"feature": "Direction_same", "instances": 9, "metric_value": 0.381, "depth": 10}
										if obj[10]<=0:
											# {"feature": "Bar", "instances": 7, "metric_value": 0.4762, "depth": 11}
											if obj[7]<=0.0:
												# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[9]<=1.0:
													return 'False'
												else: return 'False'
											elif obj[7]>0.0:
												# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[9]<=4.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[10]>0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[1]>3:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[6]>18.296160208955353:
						# {"feature": "Age", "instances": 124, "metric_value": 0.2839, "depth": 6}
						if obj[4]>0:
							# {"feature": "Bar", "instances": 98, "metric_value": 0.3358, "depth": 7}
							if obj[7]<=2.0:
								# {"feature": "Time", "instances": 84, "metric_value": 0.2981, "depth": 8}
								if obj[1]<=1:
									# {"feature": "Direction_same", "instances": 53, "metric_value": 0.3541, "depth": 9}
									if obj[10]>0:
										# {"feature": "Education", "instances": 30, "metric_value": 0.2407, "depth": 10}
										if obj[5]<=2:
											# {"feature": "Gender", "instances": 18, "metric_value": 0.1026, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.1368, "depth": 12}
												if obj[9]<=1.0:
													return 'True'
												elif obj[9]>1.0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												return 'True'
											else: return 'True'
										elif obj[5]>2:
											# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.419, "depth": 11}
											if obj[9]>1.0:
												# {"feature": "Gender", "instances": 7, "metric_value": 0.4762, "depth": 12}
												if obj[3]<=0:
													return 'False'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											elif obj[9]<=1.0:
												# {"feature": "Gender", "instances": 5, "metric_value": 0.2667, "depth": 12}
												if obj[3]>0:
													return 'True'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[10]<=0:
										# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.4174, "depth": 10}
										if obj[9]<=2.0:
											# {"feature": "Education", "instances": 20, "metric_value": 0.4533, "depth": 11}
											if obj[5]<=2:
												# {"feature": "Gender", "instances": 15, "metric_value": 0.4933, "depth": 12}
												if obj[3]>0:
													return 'False'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											elif obj[5]>2:
												# {"feature": "Gender", "instances": 5, "metric_value": 0.3, "depth": 12}
												if obj[3]<=0:
													return 'True'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[9]>2.0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[1]>1:
									# {"feature": "Direction_same", "instances": 31, "metric_value": 0.1628, "depth": 9}
									if obj[10]<=0:
										# {"feature": "Restaurant20to50", "instances": 28, "metric_value": 0.122, "depth": 10}
										if obj[9]>0.0:
											# {"feature": "Education", "instances": 24, "metric_value": 0.075, "depth": 11}
											if obj[5]<=2:
												return 'True'
											elif obj[5]>2:
												# {"feature": "Gender", "instances": 10, "metric_value": 0.16, "depth": 12}
												if obj[3]<=0:
													return 'True'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[9]<=0.0:
											# {"feature": "Gender", "instances": 4, "metric_value": 0.375, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Education", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[5]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[10]>0:
										# {"feature": "Gender", "instances": 3, "metric_value": 0.3333, "depth": 10}
										if obj[3]>0:
											# {"feature": "Education", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[5]<=3:
												# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[9]<=1.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[7]>2.0:
								# {"feature": "Time", "instances": 14, "metric_value": 0.3636, "depth": 8}
								if obj[1]<=3:
									# {"feature": "Direction_same", "instances": 11, "metric_value": 0.3117, "depth": 9}
									if obj[10]>0:
										# {"feature": "Education", "instances": 7, "metric_value": 0.4762, "depth": 10}
										if obj[5]>0:
											# {"feature": "Gender", "instances": 4, "metric_value": 0.5, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[9]<=2.0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[5]<=0:
											# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[9]<=2.0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[10]<=0:
										return 'True'
									else: return 'True'
								elif obj[1]>3:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[4]<=0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[0]>2:
					# {"feature": "Time", "instances": 882, "metric_value": 0.3365, "depth": 5}
					if obj[1]<=2:
						# {"feature": "Bar", "instances": 545, "metric_value": 0.2856, "depth": 6}
						if obj[7]<=3.0:
							# {"feature": "Occupation", "instances": 507, "metric_value": 0.2689, "depth": 7}
							if obj[6]<=17.929550223445236:
								# {"feature": "Education", "instances": 475, "metric_value": 0.2809, "depth": 8}
								if obj[5]<=3:
									# {"feature": "Age", "instances": 449, "metric_value": 0.2917, "depth": 9}
									if obj[4]<=5:
										# {"feature": "Restaurant20to50", "instances": 371, "metric_value": 0.2754, "depth": 10}
										if obj[9]<=2.0:
											# {"feature": "Gender", "instances": 345, "metric_value": 0.264, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 181, "metric_value": 0.2615, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 164, "metric_value": 0.2668, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[9]>2.0:
											# {"feature": "Gender", "instances": 26, "metric_value": 0.4203, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 14, "metric_value": 0.4592, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 12, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[4]>5:
										# {"feature": "Restaurant20to50", "instances": 78, "metric_value": 0.3493, "depth": 10}
										if obj[9]<=2.0:
											# {"feature": "Gender", "instances": 74, "metric_value": 0.3682, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 41, "metric_value": 0.3688, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 33, "metric_value": 0.3673, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[9]>2.0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[5]>3:
									# {"feature": "Age", "instances": 26, "metric_value": 0.0673, "depth": 9}
									if obj[4]<=3:
										return 'True'
									elif obj[4]>3:
										# {"feature": "Gender", "instances": 8, "metric_value": 0.1875, "depth": 10}
										if obj[3]>0:
											return 'True'
										elif obj[3]<=0:
											# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.25, "depth": 11}
											if obj[9]<=0.0:
												return 'True'
											elif obj[9]>0.0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[6]>17.929550223445236:
								# {"feature": "Age", "instances": 32, "metric_value": 0.0536, "depth": 8}
								if obj[4]<=1:
									return 'True'
								elif obj[4]>1:
									# {"feature": "Education", "instances": 7, "metric_value": 0.1905, "depth": 9}
									if obj[5]<=0:
										return 'True'
									elif obj[5]>0:
										# {"feature": "Gender", "instances": 3, "metric_value": 0.0, "depth": 10}
										if obj[3]>0:
											return 'True'
										elif obj[3]<=0:
											return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[7]>3.0:
							# {"feature": "Restaurant20to50", "instances": 38, "metric_value": 0.4369, "depth": 7}
							if obj[9]>1.0:
								# {"feature": "Occupation", "instances": 22, "metric_value": 0.3463, "depth": 8}
								if obj[6]<=14:
									# {"feature": "Age", "instances": 21, "metric_value": 0.3361, "depth": 9}
									if obj[4]>0:
										# {"feature": "Gender", "instances": 17, "metric_value": 0.3832, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Education", "instances": 10, "metric_value": 0.48, "depth": 11}
											if obj[5]>0:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[5]<=0:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]>0:
											# {"feature": "Education", "instances": 7, "metric_value": 0.2381, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 0.2778, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[5]>0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[4]<=0:
										return 'True'
									else: return 'True'
								elif obj[6]>14:
									return 'False'
								else: return 'False'
							elif obj[9]<=1.0:
								# {"feature": "Age", "instances": 16, "metric_value": 0.45, "depth": 8}
								if obj[4]>0:
									# {"feature": "Gender", "instances": 15, "metric_value": 0.4778, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Education", "instances": 12, "metric_value": 0.4857, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Occupation", "instances": 7, "metric_value": 0.4898, "depth": 11}
											if obj[6]<=18:
												# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4898, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[5]>0:
											# {"feature": "Occupation", "instances": 5, "metric_value": 0.48, "depth": 11}
											if obj[6]<=2:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[3]>0:
										# {"feature": "Education", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Occupation", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[6]<=7:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[4]<=0:
									return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'True'
					elif obj[1]>2:
						# {"feature": "Age", "instances": 337, "metric_value": 0.3985, "depth": 6}
						if obj[4]<=3:
							# {"feature": "Bar", "instances": 189, "metric_value": 0.4407, "depth": 7}
							if obj[7]<=3.0:
								# {"feature": "Education", "instances": 182, "metric_value": 0.4334, "depth": 8}
								if obj[5]<=3:
									# {"feature": "Occupation", "instances": 170, "metric_value": 0.4475, "depth": 9}
									if obj[6]>1:
										# {"feature": "Restaurant20to50", "instances": 150, "metric_value": 0.4599, "depth": 10}
										if obj[9]>0.0:
											# {"feature": "Gender", "instances": 141, "metric_value": 0.4571, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 81, "metric_value": 0.4664, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 60, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[9]<=0.0:
											# {"feature": "Gender", "instances": 9, "metric_value": 0.3444, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[6]<=1:
										# {"feature": "Restaurant20to50", "instances": 20, "metric_value": 0.3, "depth": 10}
										if obj[9]>0.0:
											# {"feature": "Gender", "instances": 16, "metric_value": 0.375, "depth": 11}
											if obj[3]<=1:
												# {"feature": "Direction_same", "instances": 16, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[9]<=0.0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[5]>3:
									# {"feature": "Occupation", "instances": 12, "metric_value": 0.0, "depth": 9}
									if obj[6]>1:
										return 'True'
									elif obj[6]<=1:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[7]>3.0:
								# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.2381, "depth": 8}
								if obj[9]>1.0:
									# {"feature": "Education", "instances": 6, "metric_value": 0.25, "depth": 9}
									if obj[5]>3:
										# {"feature": "Gender", "instances": 4, "metric_value": 0.375, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Occupation", "instances": 4, "metric_value": 0.375, "depth": 11}
											if obj[6]<=1:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[5]<=3:
										return 'False'
									else: return 'False'
								elif obj[9]<=1.0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[4]>3:
							# {"feature": "Restaurant20to50", "instances": 148, "metric_value": 0.3203, "depth": 7}
							if obj[9]<=1.0:
								# {"feature": "Gender", "instances": 84, "metric_value": 0.3607, "depth": 8}
								if obj[3]<=0:
									# {"feature": "Bar", "instances": 53, "metric_value": 0.2614, "depth": 9}
									if obj[7]<=1.0:
										# {"feature": "Occupation", "instances": 33, "metric_value": 0.1437, "depth": 10}
										if obj[6]<=7:
											# {"feature": "Education", "instances": 31, "metric_value": 0.1191, "depth": 11}
											if obj[5]<=2:
												# {"feature": "Direction_same", "instances": 26, "metric_value": 0.142, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[5]>2:
												return 'True'
											else: return 'True'
										elif obj[6]>7:
											# {"feature": "Education", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[5]<=3:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[7]>1.0:
										# {"feature": "Occupation", "instances": 20, "metric_value": 0.3111, "depth": 10}
										if obj[6]>1:
											# {"feature": "Education", "instances": 18, "metric_value": 0.3377, "depth": 11}
											if obj[5]>0:
												# {"feature": "Direction_same", "instances": 11, "metric_value": 0.3967, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[5]<=0:
												# {"feature": "Direction_same", "instances": 7, "metric_value": 0.2449, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[6]<=1:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[3]>0:
									# {"feature": "Occupation", "instances": 31, "metric_value": 0.4516, "depth": 9}
									if obj[6]>0:
										# {"feature": "Bar", "instances": 28, "metric_value": 0.44, "depth": 10}
										if obj[7]<=2.0:
											# {"feature": "Education", "instances": 25, "metric_value": 0.4753, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Direction_same", "instances": 14, "metric_value": 0.4592, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[5]>0:
												# {"feature": "Direction_same", "instances": 11, "metric_value": 0.4959, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[7]>2.0:
											return 'True'
										else: return 'True'
									elif obj[6]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[9]>1.0:
								# {"feature": "Gender", "instances": 64, "metric_value": 0.205, "depth": 8}
								if obj[3]>0:
									# {"feature": "Bar", "instances": 37, "metric_value": 0.0885, "depth": 9}
									if obj[7]<=2.0:
										# {"feature": "Education", "instances": 34, "metric_value": 0.0546, "depth": 10}
										if obj[5]>0:
											return 'True'
										elif obj[5]<=0:
											# {"feature": "Occupation", "instances": 14, "metric_value": 0.125, "depth": 11}
											if obj[6]>6:
												# {"feature": "Direction_same", "instances": 8, "metric_value": 0.2188, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[6]<=6:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[7]>2.0:
										# {"feature": "Education", "instances": 3, "metric_value": 0.0, "depth": 10}
										if obj[5]<=2:
											return 'True'
										elif obj[5]>2:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[3]<=0:
									# {"feature": "Bar", "instances": 27, "metric_value": 0.3333, "depth": 9}
									if obj[7]>0.0:
										# {"feature": "Education", "instances": 24, "metric_value": 0.3632, "depth": 10}
										if obj[5]>0:
											# {"feature": "Occupation", "instances": 19, "metric_value": 0.3218, "depth": 11}
											if obj[6]>7:
												# {"feature": "Direction_same", "instances": 11, "metric_value": 0.3967, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[6]<=7:
												# {"feature": "Direction_same", "instances": 8, "metric_value": 0.2188, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[5]<=0:
											# {"feature": "Occupation", "instances": 5, "metric_value": 0.4, "depth": 11}
											if obj[6]<=7:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[6]>7:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[7]<=0.0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[11]>2:
				# {"feature": "Education", "instances": 281, "metric_value": 0.4772, "depth": 4}
				if obj[5]>0:
					# {"feature": "Age", "instances": 199, "metric_value": 0.4637, "depth": 5}
					if obj[4]<=4:
						# {"feature": "Occupation", "instances": 174, "metric_value": 0.4818, "depth": 6}
						if obj[6]<=11:
							# {"feature": "Passanger", "instances": 141, "metric_value": 0.4783, "depth": 7}
							if obj[0]>0:
								# {"feature": "Restaurant20to50", "instances": 137, "metric_value": 0.4729, "depth": 8}
								if obj[9]<=2.0:
									# {"feature": "Bar", "instances": 120, "metric_value": 0.4949, "depth": 9}
									if obj[7]>0.0:
										# {"feature": "Gender", "instances": 83, "metric_value": 0.4622, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Time", "instances": 49, "metric_value": 0.463, "depth": 11}
											if obj[1]<=1:
												# {"feature": "Direction_same", "instances": 39, "metric_value": 0.4997, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[1]>1:
												# {"feature": "Direction_same", "instances": 10, "metric_value": 0.32, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]>0:
											# {"feature": "Time", "instances": 34, "metric_value": 0.3782, "depth": 11}
											if obj[1]>0:
												# {"feature": "Direction_same", "instances": 28, "metric_value": 0.4592, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[1]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[7]<=0.0:
										# {"feature": "Gender", "instances": 37, "metric_value": 0.4702, "depth": 10}
										if obj[3]>0:
											# {"feature": "Time", "instances": 26, "metric_value": 0.4487, "depth": 11}
											if obj[1]>0:
												# {"feature": "Direction_same", "instances": 24, "metric_value": 0.4861, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[1]<=0:
												return 'True'
											else: return 'True'
										elif obj[3]<=0:
											# {"feature": "Time", "instances": 11, "metric_value": 0.3636, "depth": 11}
											if obj[1]>0:
												# {"feature": "Direction_same", "instances": 8, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[1]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[9]>2.0:
									# {"feature": "Time", "instances": 17, "metric_value": 0.0882, "depth": 9}
									if obj[1]<=1:
										return 'False'
									elif obj[1]>1:
										# {"feature": "Bar", "instances": 4, "metric_value": 0.0, "depth": 10}
										if obj[7]>1.0:
											return 'True'
										elif obj[7]<=1.0:
											return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'False'
							elif obj[0]<=0:
								return 'True'
							else: return 'True'
						elif obj[6]>11:
							# {"feature": "Restaurant20to50", "instances": 33, "metric_value": 0.3673, "depth": 7}
							if obj[9]<=3.0:
								# {"feature": "Bar", "instances": 29, "metric_value": 0.3291, "depth": 8}
								if obj[7]<=2.0:
									# {"feature": "Time", "instances": 20, "metric_value": 0.2471, "depth": 9}
									if obj[1]>0:
										# {"feature": "Gender", "instances": 17, "metric_value": 0.2906, "depth": 10}
										if obj[3]>0:
											# {"feature": "Passanger", "instances": 11, "metric_value": 0.2975, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 11, "metric_value": 0.2975, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]<=0:
											# {"feature": "Passanger", "instances": 6, "metric_value": 0.2778, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 0.2778, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[1]<=0:
										return 'True'
									else: return 'True'
								elif obj[7]>2.0:
									# {"feature": "Time", "instances": 9, "metric_value": 0.3175, "depth": 9}
									if obj[1]>0:
										# {"feature": "Gender", "instances": 7, "metric_value": 0.2857, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Passanger", "instances": 4, "metric_value": 0.5, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]>0:
											return 'True'
										else: return 'True'
									elif obj[1]<=0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[9]>3.0:
								# {"feature": "Gender", "instances": 4, "metric_value": 0.25, "depth": 8}
								if obj[3]<=0:
									return 'False'
								elif obj[3]>0:
									# {"feature": "Passanger", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Time", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[1]<=1:
											# {"feature": "Bar", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[7]<=2.0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[4]>4:
						# {"feature": "Occupation", "instances": 25, "metric_value": 0.1467, "depth": 6}
						if obj[6]<=16:
							# {"feature": "Bar", "instances": 24, "metric_value": 0.1417, "depth": 7}
							if obj[7]<=1.0:
								# {"feature": "Restaurant20to50", "instances": 20, "metric_value": 0.0909, "depth": 8}
								if obj[9]>1.0:
									# {"feature": "Gender", "instances": 11, "metric_value": 0.1515, "depth": 9}
									if obj[3]>0:
										# {"feature": "Time", "instances": 6, "metric_value": 0.25, "depth": 10}
										if obj[1]<=1:
											# {"feature": "Passanger", "instances": 4, "metric_value": 0.375, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[1]>1:
											return 'False'
										else: return 'False'
									elif obj[3]<=0:
										return 'False'
									else: return 'False'
								elif obj[9]<=1.0:
									return 'False'
								else: return 'False'
							elif obj[7]>1.0:
								# {"feature": "Gender", "instances": 4, "metric_value": 0.25, "depth": 8}
								if obj[3]>0:
									return 'False'
								elif obj[3]<=0:
									# {"feature": "Passanger", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Time", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[1]<=1:
											# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[9]<=2.0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[6]>16:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[5]<=0:
					# {"feature": "Occupation", "instances": 82, "metric_value": 0.4027, "depth": 5}
					if obj[6]>4:
						# {"feature": "Age", "instances": 62, "metric_value": 0.4622, "depth": 6}
						if obj[4]<=6:
							# {"feature": "Restaurant20to50", "instances": 61, "metric_value": 0.4568, "depth": 7}
							if obj[9]<=3.0:
								# {"feature": "Gender", "instances": 60, "metric_value": 0.4568, "depth": 8}
								if obj[3]<=0:
									# {"feature": "Bar", "instances": 35, "metric_value": 0.4038, "depth": 9}
									if obj[7]<=2.0:
										# {"feature": "Time", "instances": 30, "metric_value": 0.3826, "depth": 10}
										if obj[1]>0:
											# {"feature": "Passanger", "instances": 22, "metric_value": 0.3512, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 22, "metric_value": 0.3512, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[1]<=0:
											# {"feature": "Passanger", "instances": 8, "metric_value": 0.4583, "depth": 11}
											if obj[0]>0:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[0]<=0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[7]>2.0:
										# {"feature": "Passanger", "instances": 5, "metric_value": 0.48, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Time", "instances": 5, "metric_value": 0.48, "depth": 11}
											if obj[1]<=1:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[3]>0:
									# {"feature": "Bar", "instances": 25, "metric_value": 0.4588, "depth": 9}
									if obj[7]<=1.0:
										# {"feature": "Passanger", "instances": 17, "metric_value": 0.4632, "depth": 10}
										if obj[0]>0:
											# {"feature": "Time", "instances": 16, "metric_value": 0.4375, "depth": 11}
											if obj[1]>0:
												# {"feature": "Direction_same", "instances": 14, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[1]<=0:
												return 'False'
											else: return 'False'
										elif obj[0]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]>1.0:
										# {"feature": "Passanger", "instances": 8, "metric_value": 0.3571, "depth": 10}
										if obj[0]>0:
											# {"feature": "Time", "instances": 7, "metric_value": 0.3714, "depth": 11}
											if obj[1]>0:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[1]<=0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[0]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[9]>3.0:
								return 'False'
							else: return 'False'
						elif obj[4]>6:
							return 'False'
						else: return 'False'
					elif obj[6]<=4:
						# {"feature": "Time", "instances": 20, "metric_value": 0.1608, "depth": 6}
						if obj[1]<=1:
							# {"feature": "Gender", "instances": 17, "metric_value": 0.0941, "depth": 7}
							if obj[3]>0:
								return 'True'
							elif obj[3]<=0:
								# {"feature": "Bar", "instances": 5, "metric_value": 0.2, "depth": 8}
								if obj[7]<=0.0:
									return 'True'
								elif obj[7]>0.0:
									# {"feature": "Passanger", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Age", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[4]<=4:
											# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[9]<=0.0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[1]>1:
							# {"feature": "Age", "instances": 3, "metric_value": 0.0, "depth": 7}
							if obj[4]>2:
								return 'True'
							elif obj[4]<=2:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[2]<=1:
		# {"feature": "Bar", "instances": 2261, "metric_value": 0.4547, "depth": 2}
		if obj[7]>0.0:
			# {"feature": "Passanger", "instances": 1286, "metric_value": 0.4891, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Time", "instances": 1095, "metric_value": 0.4916, "depth": 4}
				if obj[1]>0:
					# {"feature": "Restaurant20to50", "instances": 757, "metric_value": 0.4869, "depth": 5}
					if obj[9]<=2.0:
						# {"feature": "Education", "instances": 686, "metric_value": 0.4848, "depth": 6}
						if obj[5]>1:
							# {"feature": "Coffeehouse", "instances": 406, "metric_value": 0.4662, "depth": 7}
							if obj[8]>1.0:
								# {"feature": "Age", "instances": 220, "metric_value": 0.4832, "depth": 8}
								if obj[4]>0:
									# {"feature": "Occupation", "instances": 195, "metric_value": 0.4939, "depth": 9}
									if obj[6]<=17:
										# {"feature": "Gender", "instances": 181, "metric_value": 0.4934, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Distance", "instances": 99, "metric_value": 0.4995, "depth": 11}
											if obj[11]>1:
												# {"feature": "Direction_same", "instances": 66, "metric_value": 0.4988, "depth": 12}
												if obj[10]<=0:
													return 'False'
												elif obj[10]>0:
													return 'False'
												else: return 'False'
											elif obj[11]<=1:
												# {"feature": "Direction_same", "instances": 33, "metric_value": 0.4995, "depth": 12}
												if obj[10]<=0:
													return 'True'
												elif obj[10]>0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[3]>0:
											# {"feature": "Direction_same", "instances": 82, "metric_value": 0.4843, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Distance", "instances": 76, "metric_value": 0.48, "depth": 12}
												if obj[11]>1:
													return 'False'
												elif obj[11]<=1:
													return 'False'
												else: return 'False'
											elif obj[10]>0:
												# {"feature": "Distance", "instances": 6, "metric_value": 0.4, "depth": 12}
												if obj[11]>1:
													return 'True'
												elif obj[11]<=1:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[6]>17:
										# {"feature": "Gender", "instances": 14, "metric_value": 0.3571, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Direction_same", "instances": 10, "metric_value": 0.4444, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Distance", "instances": 9, "metric_value": 0.4815, "depth": 12}
												if obj[11]<=2:
													return 'True'
												elif obj[11]>2:
													return 'False'
												else: return 'False'
											elif obj[10]>0:
												return 'True'
											else: return 'True'
										elif obj[3]>0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[4]<=0:
									# {"feature": "Distance", "instances": 25, "metric_value": 0.3284, "depth": 9}
									if obj[11]<=2:
										# {"feature": "Occupation", "instances": 19, "metric_value": 0.4087, "depth": 10}
										if obj[6]>1:
											# {"feature": "Gender", "instances": 17, "metric_value": 0.4373, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 12, "metric_value": 0.4815, "depth": 12}
												if obj[10]<=0:
													return 'False'
												elif obj[10]>0:
													return 'False'
												else: return 'False'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.3, "depth": 12}
												if obj[10]<=0:
													return 'False'
												elif obj[10]>0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[6]<=1:
											return 'False'
										else: return 'False'
									elif obj[11]>2:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[8]<=1.0:
								# {"feature": "Age", "instances": 186, "metric_value": 0.4154, "depth": 8}
								if obj[4]<=4:
									# {"feature": "Occupation", "instances": 144, "metric_value": 0.4306, "depth": 9}
									if obj[6]>5:
										# {"feature": "Gender", "instances": 109, "metric_value": 0.4056, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Distance", "instances": 59, "metric_value": 0.4162, "depth": 11}
											if obj[11]>1:
												# {"feature": "Direction_same", "instances": 36, "metric_value": 0.4983, "depth": 12}
												if obj[10]<=0:
													return 'False'
												elif obj[10]>0:
													return 'False'
												else: return 'False'
											elif obj[11]<=1:
												# {"feature": "Direction_same", "instances": 23, "metric_value": 0.2705, "depth": 12}
												if obj[10]<=0:
													return 'False'
												elif obj[10]>0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[3]>0:
											# {"feature": "Distance", "instances": 50, "metric_value": 0.3087, "depth": 11}
											if obj[11]<=1:
												# {"feature": "Direction_same", "instances": 26, "metric_value": 0.4185, "depth": 12}
												if obj[10]<=0:
													return 'False'
												elif obj[10]>0:
													return 'True'
												else: return 'True'
											elif obj[11]>1:
												# {"feature": "Direction_same", "instances": 24, "metric_value": 0.1491, "depth": 12}
												if obj[10]<=0:
													return 'False'
												elif obj[10]>0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[6]<=5:
										# {"feature": "Direction_same", "instances": 35, "metric_value": 0.4484, "depth": 10}
										if obj[10]<=0:
											# {"feature": "Gender", "instances": 31, "metric_value": 0.4469, "depth": 11}
											if obj[3]>0:
												# {"feature": "Distance", "instances": 20, "metric_value": 0.4125, "depth": 12}
												if obj[11]>1:
													return 'True'
												elif obj[11]<=1:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Distance", "instances": 11, "metric_value": 0.4935, "depth": 12}
												if obj[11]<=2:
													return 'True'
												elif obj[11]>2:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[10]>0:
											# {"feature": "Gender", "instances": 4, "metric_value": 0.0, "depth": 11}
											if obj[3]>0:
												return 'False'
											elif obj[3]<=0:
												return 'True'
											else: return 'True'
										else: return 'False'
									else: return 'True'
								elif obj[4]>4:
									# {"feature": "Gender", "instances": 42, "metric_value": 0.2138, "depth": 9}
									if obj[3]>0:
										# {"feature": "Occupation", "instances": 25, "metric_value": 0.0667, "depth": 10}
										if obj[6]<=6:
											return 'False'
										elif obj[6]>6:
											# {"feature": "Distance", "instances": 6, "metric_value": 0.2667, "depth": 11}
											if obj[11]>1:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[11]<=1:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[3]<=0:
										# {"feature": "Occupation", "instances": 17, "metric_value": 0.2824, "depth": 10}
										if obj[6]>5:
											# {"feature": "Distance", "instances": 15, "metric_value": 0.2667, "depth": 11}
											if obj[11]>1:
												# {"feature": "Direction_same", "instances": 9, "metric_value": 0.3333, "depth": 12}
												if obj[10]<=0:
													return 'False'
												elif obj[10]>0:
													return 'True'
												else: return 'True'
											elif obj[11]<=1:
												return 'False'
											else: return 'False'
										elif obj[6]<=5:
											return 'True'
										else: return 'True'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[5]<=1:
							# {"feature": "Occupation", "instances": 280, "metric_value": 0.4946, "depth": 7}
							if obj[6]>0:
								# {"feature": "Coffeehouse", "instances": 277, "metric_value": 0.4954, "depth": 8}
								if obj[8]<=3.0:
									# {"feature": "Age", "instances": 251, "metric_value": 0.4933, "depth": 9}
									if obj[4]<=3:
										# {"feature": "Distance", "instances": 151, "metric_value": 0.4886, "depth": 10}
										if obj[11]<=2:
											# {"feature": "Direction_same", "instances": 109, "metric_value": 0.4968, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Gender", "instances": 92, "metric_value": 0.4988, "depth": 12}
												if obj[3]<=0:
													return 'True'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											elif obj[10]>0:
												# {"feature": "Gender", "instances": 17, "metric_value": 0.4189, "depth": 12}
												if obj[3]<=0:
													return 'True'
												elif obj[3]>0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[11]>2:
											# {"feature": "Gender", "instances": 42, "metric_value": 0.4558, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 22, "metric_value": 0.4339, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 20, "metric_value": 0.48, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[4]>3:
										# {"feature": "Distance", "instances": 100, "metric_value": 0.4446, "depth": 10}
										if obj[11]<=2:
											# {"feature": "Direction_same", "instances": 67, "metric_value": 0.4937, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Gender", "instances": 57, "metric_value": 0.4871, "depth": 12}
												if obj[3]<=0:
													return 'True'
												elif obj[3]>0:
													return 'False'
												else: return 'False'
											elif obj[10]>0:
												# {"feature": "Gender", "instances": 10, "metric_value": 0.4667, "depth": 12}
												if obj[3]>0:
													return 'True'
												elif obj[3]<=0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[11]>2:
											# {"feature": "Gender", "instances": 33, "metric_value": 0.3342, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 19, "metric_value": 0.3324, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 14, "metric_value": 0.3367, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[8]>3.0:
									# {"feature": "Distance", "instances": 26, "metric_value": 0.3546, "depth": 9}
									if obj[11]<=2:
										# {"feature": "Age", "instances": 21, "metric_value": 0.3274, "depth": 10}
										if obj[4]<=4:
											# {"feature": "Direction_same", "instances": 16, "metric_value": 0.3846, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Gender", "instances": 13, "metric_value": 0.4685, "depth": 12}
												if obj[3]>0:
													return 'False'
												elif obj[3]<=0:
													return 'False'
												else: return 'False'
											elif obj[10]>0:
												return 'False'
											else: return 'False'
										elif obj[4]>4:
											return 'False'
										else: return 'False'
									elif obj[11]>2:
										# {"feature": "Gender", "instances": 5, "metric_value": 0.2667, "depth": 10}
										if obj[3]>0:
											# {"feature": "Age", "instances": 3, "metric_value": 0.3333, "depth": 11}
											if obj[4]>1:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[4]<=1:
												return 'True'
											else: return 'True'
										elif obj[3]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[6]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[9]>2.0:
						# {"feature": "Occupation", "instances": 71, "metric_value": 0.4231, "depth": 6}
						if obj[6]<=14:
							# {"feature": "Gender", "instances": 59, "metric_value": 0.3956, "depth": 7}
							if obj[3]<=0:
								# {"feature": "Education", "instances": 33, "metric_value": 0.2754, "depth": 8}
								if obj[5]<=2:
									# {"feature": "Distance", "instances": 18, "metric_value": 0.0833, "depth": 9}
									if obj[11]<=2:
										return 'True'
									elif obj[11]>2:
										# {"feature": "Age", "instances": 4, "metric_value": 0.25, "depth": 10}
										if obj[4]<=2:
											return 'True'
										elif obj[4]>2:
											# {"feature": "Coffeehouse", "instances": 2, "metric_value": 0.0, "depth": 11}
											if obj[8]<=2.0:
												return 'True'
											elif obj[8]>2.0:
												return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'True'
								elif obj[5]>2:
									# {"feature": "Direction_same", "instances": 15, "metric_value": 0.3692, "depth": 9}
									if obj[10]<=0:
										# {"feature": "Age", "instances": 13, "metric_value": 0.2521, "depth": 10}
										if obj[4]>0:
											# {"feature": "Distance", "instances": 9, "metric_value": 0.1667, "depth": 11}
											if obj[11]>1:
												return 'True'
											elif obj[11]<=1:
												# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.3333, "depth": 12}
												if obj[8]>1.0:
													return 'True'
												elif obj[8]<=1.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[4]<=0:
											# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.0, "depth": 11}
											if obj[8]<=2.0:
												return 'False'
											elif obj[8]>2.0:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[10]>0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[3]>0:
								# {"feature": "Education", "instances": 26, "metric_value": 0.3846, "depth": 8}
								if obj[5]<=3:
									# {"feature": "Age", "instances": 20, "metric_value": 0.4545, "depth": 9}
									if obj[4]>2:
										# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.3117, "depth": 10}
										if obj[8]<=2.0:
											# {"feature": "Distance", "instances": 7, "metric_value": 0.4048, "depth": 11}
											if obj[11]<=1:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.3333, "depth": 12}
												if obj[10]<=0:
													return 'True'
												elif obj[10]>0:
													return 'True'
												else: return 'True'
											elif obj[11]>1:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[8]>2.0:
											return 'False'
										else: return 'False'
									elif obj[4]<=2:
										# {"feature": "Direction_same", "instances": 9, "metric_value": 0.3333, "depth": 10}
										if obj[10]<=0:
											# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.3333, "depth": 11}
											if obj[8]<=3.0:
												# {"feature": "Distance", "instances": 6, "metric_value": 0.4167, "depth": 12}
												if obj[11]>1:
													return 'True'
												elif obj[11]<=1:
													return 'True'
												else: return 'True'
											elif obj[8]>3.0:
												return 'True'
											else: return 'True'
										elif obj[10]>0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[5]>3:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[6]>14:
							# {"feature": "Education", "instances": 12, "metric_value": 0.3125, "depth": 7}
							if obj[5]<=2:
								# {"feature": "Age", "instances": 8, "metric_value": 0.1875, "depth": 8}
								if obj[4]<=0:
									# {"feature": "Distance", "instances": 4, "metric_value": 0.0, "depth": 9}
									if obj[11]<=2:
										return 'False'
									elif obj[11]>2:
										return 'True'
									else: return 'True'
								elif obj[4]>0:
									return 'True'
								else: return 'True'
							elif obj[5]>2:
								return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[1]<=0:
					# {"feature": "Distance", "instances": 338, "metric_value": 0.4678, "depth": 5}
					if obj[11]>1:
						# {"feature": "Direction_same", "instances": 182, "metric_value": 0.485, "depth": 6}
						if obj[10]<=0:
							# {"feature": "Age", "instances": 171, "metric_value": 0.4792, "depth": 7}
							if obj[4]>1:
								# {"feature": "Restaurant20to50", "instances": 111, "metric_value": 0.4878, "depth": 8}
								if obj[9]<=1.0:
									# {"feature": "Occupation", "instances": 68, "metric_value": 0.4642, "depth": 9}
									if obj[6]>5:
										# {"feature": "Coffeehouse", "instances": 43, "metric_value": 0.4927, "depth": 10}
										if obj[8]>0.0:
											# {"feature": "Education", "instances": 31, "metric_value": 0.4817, "depth": 11}
											if obj[5]<=3:
												# {"feature": "Gender", "instances": 30, "metric_value": 0.4889, "depth": 12}
												if obj[3]<=0:
													return 'False'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											elif obj[5]>3:
												return 'False'
											else: return 'False'
										elif obj[8]<=0.0:
											# {"feature": "Education", "instances": 12, "metric_value": 0.3704, "depth": 11}
											if obj[5]>0:
												# {"feature": "Gender", "instances": 9, "metric_value": 0.4815, "depth": 12}
												if obj[3]<=0:
													return 'False'
												elif obj[3]>0:
													return 'False'
												else: return 'False'
											elif obj[5]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[6]<=5:
										# {"feature": "Education", "instances": 25, "metric_value": 0.36, "depth": 10}
										if obj[5]<=3:
											# {"feature": "Coffeehouse", "instances": 24, "metric_value": 0.3667, "depth": 11}
											if obj[8]<=2.0:
												# {"feature": "Gender", "instances": 15, "metric_value": 0.3071, "depth": 12}
												if obj[3]>0:
													return 'False'
												elif obj[3]<=0:
													return 'False'
												else: return 'False'
											elif obj[8]>2.0:
												# {"feature": "Gender", "instances": 9, "metric_value": 0.381, "depth": 12}
												if obj[3]>0:
													return 'False'
												elif obj[3]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[5]>3:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[9]>1.0:
									# {"feature": "Education", "instances": 43, "metric_value": 0.4542, "depth": 9}
									if obj[5]>0:
										# {"feature": "Coffeehouse", "instances": 29, "metric_value": 0.415, "depth": 10}
										if obj[8]>0.0:
											# {"feature": "Gender", "instances": 21, "metric_value": 0.4259, "depth": 11}
											if obj[3]>0:
												# {"feature": "Occupation", "instances": 12, "metric_value": 0.4444, "depth": 12}
												if obj[6]<=16:
													return 'False'
												elif obj[6]>16:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Occupation", "instances": 9, "metric_value": 0.2667, "depth": 12}
												if obj[6]>6:
													return 'True'
												elif obj[6]<=6:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[8]<=0.0:
											# {"feature": "Occupation", "instances": 8, "metric_value": 0.0, "depth": 11}
											if obj[6]>6:
												return 'True'
											elif obj[6]<=6:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[5]<=0:
										# {"feature": "Coffeehouse", "instances": 14, "metric_value": 0.3571, "depth": 10}
										if obj[8]>1.0:
											# {"feature": "Occupation", "instances": 10, "metric_value": 0.375, "depth": 11}
											if obj[6]<=12:
												# {"feature": "Gender", "instances": 8, "metric_value": 0.4375, "depth": 12}
												if obj[3]>0:
													return 'True'
												elif obj[3]<=0:
													return 'False'
												else: return 'False'
											elif obj[6]>12:
												return 'True'
											else: return 'True'
										elif obj[8]<=1.0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[4]<=1:
								# {"feature": "Occupation", "instances": 60, "metric_value": 0.3907, "depth": 8}
								if obj[6]>3:
									# {"feature": "Education", "instances": 50, "metric_value": 0.3698, "depth": 9}
									if obj[5]<=3:
										# {"feature": "Restaurant20to50", "instances": 45, "metric_value": 0.3879, "depth": 10}
										if obj[9]<=3.0:
											# {"feature": "Coffeehouse", "instances": 44, "metric_value": 0.3864, "depth": 11}
											if obj[8]<=3.0:
												# {"feature": "Gender", "instances": 40, "metric_value": 0.3722, "depth": 12}
												if obj[3]>0:
													return 'True'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											elif obj[8]>3.0:
												# {"feature": "Gender", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[3]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[9]>3.0:
											return 'False'
										else: return 'False'
									elif obj[5]>3:
										return 'True'
									else: return 'True'
								elif obj[6]<=3:
									# {"feature": "Gender", "instances": 10, "metric_value": 0.175, "depth": 9}
									if obj[3]>0:
										# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.1875, "depth": 10}
										if obj[8]>1.0:
											return 'False'
										elif obj[8]<=1.0:
											# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.25, "depth": 11}
											if obj[9]>1.0:
												# {"feature": "Education", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[5]<=0:
													return 'True'
												else: return 'True'
											elif obj[9]<=1.0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[3]<=0:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'True'
						elif obj[10]>0:
							# {"feature": "Occupation", "instances": 11, "metric_value": 0.2424, "depth": 7}
							if obj[6]<=6:
								# {"feature": "Age", "instances": 6, "metric_value": 0.3333, "depth": 8}
								if obj[4]>0:
									# {"feature": "Gender", "instances": 4, "metric_value": 0.3333, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Education", "instances": 3, "metric_value": 0.0, "depth": 10}
										if obj[5]>0:
											return 'False'
										elif obj[5]<=0:
											return 'True'
										else: return 'True'
									elif obj[3]>0:
										return 'True'
									else: return 'True'
								elif obj[4]<=0:
									return 'False'
								else: return 'False'
							elif obj[6]>6:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[11]<=1:
						# {"feature": "Direction_same", "instances": 156, "metric_value": 0.4105, "depth": 6}
						if obj[10]>0:
							# {"feature": "Restaurant20to50", "instances": 146, "metric_value": 0.3926, "depth": 7}
							if obj[9]<=1.0:
								# {"feature": "Education", "instances": 92, "metric_value": 0.4484, "depth": 8}
								if obj[5]<=3:
									# {"feature": "Age", "instances": 88, "metric_value": 0.4588, "depth": 9}
									if obj[4]<=6:
										# {"feature": "Gender", "instances": 85, "metric_value": 0.4617, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Occupation", "instances": 50, "metric_value": 0.425, "depth": 11}
											if obj[6]>2.9388214248136357:
												# {"feature": "Coffeehouse", "instances": 43, "metric_value": 0.4485, "depth": 12}
												if obj[8]>-1.0:
													return 'True'
												elif obj[8]<=-1.0:
													return 'True'
												else: return 'True'
											elif obj[6]<=2.9388214248136357:
												# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.2143, "depth": 12}
												if obj[8]>1.0:
													return 'True'
												elif obj[8]<=1.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]>0:
											# {"feature": "Occupation", "instances": 35, "metric_value": 0.4797, "depth": 11}
											if obj[6]>4:
												# {"feature": "Coffeehouse", "instances": 22, "metric_value": 0.4173, "depth": 12}
												if obj[8]<=2.0:
													return 'False'
												elif obj[8]>2.0:
													return 'True'
												else: return 'True'
											elif obj[6]<=4:
												# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.4487, "depth": 12}
												if obj[8]<=3.0:
													return 'False'
												elif obj[8]>3.0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[4]>6:
										return 'True'
									else: return 'True'
								elif obj[5]>3:
									return 'True'
								else: return 'True'
							elif obj[9]>1.0:
								# {"feature": "Education", "instances": 54, "metric_value": 0.2516, "depth": 8}
								if obj[5]<=4:
									# {"feature": "Occupation", "instances": 53, "metric_value": 0.2478, "depth": 9}
									if obj[6]<=20:
										# {"feature": "Age", "instances": 47, "metric_value": 0.2138, "depth": 10}
										if obj[4]<=2:
											# {"feature": "Gender", "instances": 27, "metric_value": 0.28, "depth": 11}
											if obj[3]>0:
												# {"feature": "Coffeehouse", "instances": 14, "metric_value": 0.3297, "depth": 12}
												if obj[8]<=3.0:
													return 'True'
												elif obj[8]>3.0:
													return 'False'
												else: return 'False'
											elif obj[3]<=0:
												# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.1319, "depth": 12}
												if obj[8]<=2.0:
													return 'True'
												elif obj[8]>2.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[4]>2:
											# {"feature": "Gender", "instances": 20, "metric_value": 0.09, "depth": 11}
											if obj[3]>0:
												return 'True'
											elif obj[3]<=0:
												# {"feature": "Coffeehouse", "instances": 10, "metric_value": 0.1667, "depth": 12}
												if obj[8]>1.0:
													return 'True'
												elif obj[8]<=1.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[6]>20:
										# {"feature": "Age", "instances": 6, "metric_value": 0.2222, "depth": 10}
										if obj[4]<=2:
											return 'True'
										elif obj[4]>2:
											# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.0, "depth": 11}
											if obj[8]<=1.0:
												return 'False'
											elif obj[8]>1.0:
												return 'True'
											else: return 'True'
										else: return 'False'
									else: return 'True'
								elif obj[5]>4:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[10]<=0:
							# {"feature": "Age", "instances": 10, "metric_value": 0.3, "depth": 7}
							if obj[4]>0:
								# {"feature": "Gender", "instances": 6, "metric_value": 0.25, "depth": 8}
								if obj[3]<=0:
									# {"feature": "Occupation", "instances": 4, "metric_value": 0.0, "depth": 9}
									if obj[6]<=9:
										return 'True'
									elif obj[6]>9:
										return 'False'
									else: return 'False'
								elif obj[3]>0:
									return 'False'
								else: return 'False'
							elif obj[4]<=0:
								return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			elif obj[0]>2:
				# {"feature": "Time", "instances": 191, "metric_value": 0.4082, "depth": 4}
				if obj[1]>2:
					# {"feature": "Occupation", "instances": 148, "metric_value": 0.3544, "depth": 5}
					if obj[6]<=7.54054054054054:
						# {"feature": "Age", "instances": 92, "metric_value": 0.3936, "depth": 6}
						if obj[4]<=5:
							# {"feature": "Coffeehouse", "instances": 81, "metric_value": 0.3926, "depth": 7}
							if obj[8]>1.0:
								# {"feature": "Education", "instances": 47, "metric_value": 0.2993, "depth": 8}
								if obj[5]<=2:
									# {"feature": "Restaurant20to50", "instances": 36, "metric_value": 0.2239, "depth": 9}
									if obj[9]>0.0:
										# {"feature": "Gender", "instances": 34, "metric_value": 0.206, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Distance", "instances": 21, "metric_value": 0.1651, "depth": 11}
											if obj[11]>1:
												# {"feature": "Direction_same", "instances": 15, "metric_value": 0.2311, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[11]<=1:
												return 'True'
											else: return 'True'
										elif obj[3]>0:
											# {"feature": "Distance", "instances": 13, "metric_value": 0.2168, "depth": 11}
											if obj[11]>1:
												# {"feature": "Direction_same", "instances": 11, "metric_value": 0.1653, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[11]<=1:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[9]<=0.0:
										# {"feature": "Gender", "instances": 2, "metric_value": 0.0, "depth": 10}
										if obj[3]>0:
											return 'True'
										elif obj[3]<=0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[5]>2:
									# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.3636, "depth": 9}
									if obj[9]<=3.0:
										# {"feature": "Gender", "instances": 9, "metric_value": 0.4, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Distance", "instances": 5, "metric_value": 0.3, "depth": 11}
											if obj[11]>1:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[11]<=1:
												return 'True'
											else: return 'True'
										elif obj[3]>0:
											# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Distance", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[11]<=2:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[9]>3.0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[8]<=1.0:
								# {"feature": "Education", "instances": 34, "metric_value": 0.3249, "depth": 8}
								if obj[5]>0:
									# {"feature": "Restaurant20to50", "instances": 22, "metric_value": 0.2597, "depth": 9}
									if obj[9]<=1.0:
										# {"feature": "Distance", "instances": 14, "metric_value": 0.3929, "depth": 10}
										if obj[11]>1:
											# {"feature": "Gender", "instances": 12, "metric_value": 0.375, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 8, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[11]<=1:
											# {"feature": "Gender", "instances": 2, "metric_value": 0.0, "depth": 11}
											if obj[3]>0:
												return 'True'
											elif obj[3]<=0:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[9]>1.0:
										return 'True'
									else: return 'True'
								elif obj[5]<=0:
									# {"feature": "Distance", "instances": 12, "metric_value": 0.3333, "depth": 9}
									if obj[11]>1:
										# {"feature": "Gender", "instances": 9, "metric_value": 0.3333, "depth": 10}
										if obj[3]>0:
											# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.2667, "depth": 11}
											if obj[9]<=1.0:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[9]>1.0:
												return 'False'
											else: return 'False'
										elif obj[3]<=0:
											# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.0, "depth": 11}
											if obj[9]>0.0:
												return 'True'
											elif obj[9]<=0.0:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[11]<=1:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[4]>5:
							# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.1818, "depth": 7}
							if obj[9]<=2.0:
								return 'False'
							elif obj[9]>2.0:
								# {"feature": "Gender", "instances": 4, "metric_value": 0.0, "depth": 8}
								if obj[3]>0:
									return 'True'
								elif obj[3]<=0:
									return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'False'
					elif obj[6]>7.54054054054054:
						# {"feature": "Coffeehouse", "instances": 56, "metric_value": 0.1676, "depth": 6}
						if obj[8]<=3.0:
							# {"feature": "Gender", "instances": 52, "metric_value": 0.1281, "depth": 7}
							if obj[3]<=0:
								# {"feature": "Age", "instances": 38, "metric_value": 0.0491, "depth": 8}
								if obj[4]>1:
									return 'True'
								elif obj[4]<=1:
									# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.1111, "depth": 9}
									if obj[9]<=1.0:
										return 'True'
									elif obj[9]>1.0:
										# {"feature": "Education", "instances": 6, "metric_value": 0.1667, "depth": 10}
										if obj[5]<=1:
											return 'True'
										elif obj[5]>1:
											# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[11]<=2:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'True'
							elif obj[3]>0:
								# {"feature": "Age", "instances": 14, "metric_value": 0.131, "depth": 8}
								if obj[4]>0:
									# {"feature": "Education", "instances": 12, "metric_value": 0.1429, "depth": 9}
									if obj[5]>0:
										# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.2143, "depth": 10}
										if obj[9]<=1.0:
											# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Distance", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[11]<=2:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[9]>1.0:
											return 'True'
										else: return 'True'
									elif obj[5]<=0:
										return 'True'
									else: return 'True'
								elif obj[4]<=0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[8]>3.0:
							# {"feature": "Gender", "instances": 4, "metric_value": 0.3333, "depth": 7}
							if obj[3]<=0:
								# {"feature": "Education", "instances": 3, "metric_value": 0.0, "depth": 8}
								if obj[5]<=3:
									return 'True'
								elif obj[5]>3:
									return 'False'
								else: return 'False'
							elif obj[3]>0:
								return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[1]<=2:
					# {"feature": "Occupation", "instances": 43, "metric_value": 0.4394, "depth": 5}
					if obj[6]<=12:
						# {"feature": "Restaurant20to50", "instances": 35, "metric_value": 0.4554, "depth": 6}
						if obj[9]>0.0:
							# {"feature": "Education", "instances": 32, "metric_value": 0.4453, "depth": 7}
							if obj[5]>1:
								# {"feature": "Coffeehouse", "instances": 24, "metric_value": 0.4398, "depth": 8}
								if obj[8]>1.0:
									# {"feature": "Gender", "instances": 18, "metric_value": 0.4861, "depth": 9}
									if obj[3]>0:
										# {"feature": "Age", "instances": 10, "metric_value": 0.4444, "depth": 10}
										if obj[4]<=4:
											# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4938, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Distance", "instances": 9, "metric_value": 0.4938, "depth": 12}
												if obj[11]<=2:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[4]>4:
											return 'False'
										else: return 'False'
									elif obj[3]<=0:
										# {"feature": "Age", "instances": 8, "metric_value": 0.4583, "depth": 10}
										if obj[4]<=4:
											# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4444, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Distance", "instances": 6, "metric_value": 0.4444, "depth": 12}
												if obj[11]<=2:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[4]>4:
											# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[11]<=2:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[8]<=1.0:
									# {"feature": "Age", "instances": 6, "metric_value": 0.2222, "depth": 9}
									if obj[4]<=2:
										return 'False'
									elif obj[4]>2:
										# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Distance", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[11]<=2:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[5]<=1:
								# {"feature": "Age", "instances": 8, "metric_value": 0.25, "depth": 8}
								if obj[4]<=2:
									# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.3333, "depth": 9}
									if obj[8]<=2.0:
										# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[3]<=1:
											# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Distance", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[11]<=2:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[8]>2.0:
										return 'False'
									else: return 'False'
								elif obj[4]>2:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[9]<=0.0:
							return 'False'
						else: return 'False'
					elif obj[6]>12:
						# {"feature": "Gender", "instances": 8, "metric_value": 0.125, "depth": 6}
						if obj[3]<=0:
							return 'True'
						elif obj[3]>0:
							# {"feature": "Age", "instances": 2, "metric_value": 0.0, "depth": 7}
							if obj[4]>3:
								return 'True'
							elif obj[4]<=3:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[7]<=0.0:
			# {"feature": "Distance", "instances": 975, "metric_value": 0.3929, "depth": 3}
			if obj[11]<=2:
				# {"feature": "Education", "instances": 797, "metric_value": 0.4115, "depth": 4}
				if obj[5]>0:
					# {"feature": "Coffeehouse", "instances": 516, "metric_value": 0.3787, "depth": 5}
					if obj[8]<=2.0:
						# {"feature": "Time", "instances": 432, "metric_value": 0.41, "depth": 6}
						if obj[1]>0:
							# {"feature": "Occupation", "instances": 290, "metric_value": 0.3772, "depth": 7}
							if obj[6]<=12.422354984562588:
								# {"feature": "Direction_same", "instances": 253, "metric_value": 0.3583, "depth": 8}
								if obj[10]<=0:
									# {"feature": "Gender", "instances": 216, "metric_value": 0.3756, "depth": 9}
									if obj[3]>0:
										# {"feature": "Age", "instances": 121, "metric_value": 0.3312, "depth": 10}
										if obj[4]<=6:
											# {"feature": "Passanger", "instances": 111, "metric_value": 0.3123, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Restaurant20to50", "instances": 61, "metric_value": 0.3668, "depth": 12}
												if obj[9]>-1.0:
													return 'False'
												elif obj[9]<=-1.0:
													return 'False'
												else: return 'False'
											elif obj[0]>1:
												# {"feature": "Restaurant20to50", "instances": 50, "metric_value": 0.2332, "depth": 12}
												if obj[9]<=1.0:
													return 'False'
												elif obj[9]>1.0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[4]>6:
											# {"feature": "Passanger", "instances": 10, "metric_value": 0.419, "depth": 11}
											if obj[0]<=2:
												# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.381, "depth": 12}
												if obj[9]<=1.0:
													return 'False'
												elif obj[9]>1.0:
													return 'False'
												else: return 'False'
											elif obj[0]>2:
												# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.0, "depth": 12}
												if obj[9]>0.0:
													return 'True'
												elif obj[9]<=0.0:
													return 'False'
												else: return 'False'
											else: return 'True'
										else: return 'False'
									elif obj[3]<=0:
										# {"feature": "Passanger", "instances": 95, "metric_value": 0.4177, "depth": 10}
										if obj[0]<=2:
											# {"feature": "Age", "instances": 70, "metric_value": 0.3918, "depth": 11}
											if obj[4]<=1:
												# {"feature": "Restaurant20to50", "instances": 35, "metric_value": 0.4177, "depth": 12}
												if obj[9]<=1.0:
													return 'False'
												elif obj[9]>1.0:
													return 'False'
												else: return 'False'
											elif obj[4]>1:
												# {"feature": "Restaurant20to50", "instances": 35, "metric_value": 0.3437, "depth": 12}
												if obj[9]>-1.0:
													return 'False'
												elif obj[9]<=-1.0:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[0]>2:
											# {"feature": "Restaurant20to50", "instances": 25, "metric_value": 0.4456, "depth": 11}
											if obj[9]>0.0:
												# {"feature": "Age", "instances": 19, "metric_value": 0.4316, "depth": 12}
												if obj[4]<=3:
													return 'False'
												elif obj[4]>3:
													return 'True'
												else: return 'True'
											elif obj[9]<=0.0:
												# {"feature": "Age", "instances": 6, "metric_value": 0.2222, "depth": 12}
												if obj[4]<=2:
													return 'False'
												elif obj[4]>2:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[10]>0:
									# {"feature": "Passanger", "instances": 37, "metric_value": 0.0956, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Age", "instances": 32, "metric_value": 0.0547, "depth": 10}
										if obj[4]>0:
											return 'False'
										elif obj[4]<=0:
											# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.0, "depth": 11}
											if obj[9]>0.0:
												return 'False'
											elif obj[9]<=0.0:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[0]>1:
										# {"feature": "Age", "instances": 5, "metric_value": 0.2, "depth": 10}
										if obj[4]>1:
											return 'True'
										elif obj[4]<=1:
											# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[3]<=1:
												# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[9]<=1.0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'False'
							elif obj[6]>12.422354984562588:
								# {"feature": "Age", "instances": 37, "metric_value": 0.3929, "depth": 8}
								if obj[4]>0:
									# {"feature": "Passanger", "instances": 24, "metric_value": 0.35, "depth": 9}
									if obj[0]<=2:
										# {"feature": "Direction_same", "instances": 20, "metric_value": 0.3059, "depth": 10}
										if obj[10]<=0:
											# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.3451, "depth": 11}
											if obj[9]<=1.0:
												# {"feature": "Gender", "instances": 15, "metric_value": 0.3643, "depth": 12}
												if obj[3]<=0:
													return 'False'
												elif obj[3]>0:
													return 'False'
												else: return 'False'
											elif obj[9]>1.0:
												return 'False'
											else: return 'False'
										elif obj[10]>0:
											return 'False'
										else: return 'False'
									elif obj[0]>2:
										# {"feature": "Gender", "instances": 4, "metric_value": 0.5, "depth": 10}
										if obj[3]>0:
											# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[9]<=1.0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[3]<=0:
											# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[9]<=2.0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[4]<=0:
									# {"feature": "Gender", "instances": 13, "metric_value": 0.2517, "depth": 9}
									if obj[3]>0:
										# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.2597, "depth": 10}
										if obj[9]>0.0:
											# {"feature": "Passanger", "instances": 7, "metric_value": 0.3714, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[0]>1:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[9]<=0.0:
											return 'True'
										else: return 'True'
									elif obj[3]<=0:
										return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'False'
						elif obj[1]<=0:
							# {"feature": "Restaurant20to50", "instances": 142, "metric_value": 0.4467, "depth": 7}
							if obj[9]>0.0:
								# {"feature": "Occupation", "instances": 101, "metric_value": 0.4682, "depth": 8}
								if obj[6]>4:
									# {"feature": "Age", "instances": 66, "metric_value": 0.4828, "depth": 9}
									if obj[4]<=5:
										# {"feature": "Direction_same", "instances": 58, "metric_value": 0.497, "depth": 10}
										if obj[10]>0:
											# {"feature": "Passanger", "instances": 29, "metric_value": 0.4916, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Gender", "instances": 26, "metric_value": 0.4731, "depth": 12}
												if obj[3]<=0:
													return 'False'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											elif obj[0]>1:
												# {"feature": "Gender", "instances": 3, "metric_value": 0.0, "depth": 12}
												if obj[3]<=0:
													return 'True'
												elif obj[3]>0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[10]<=0:
											# {"feature": "Passanger", "instances": 29, "metric_value": 0.4878, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Gender", "instances": 23, "metric_value": 0.4976, "depth": 12}
												if obj[3]>0:
													return 'False'
												elif obj[3]<=0:
													return 'False'
												else: return 'False'
											elif obj[0]>1:
												# {"feature": "Gender", "instances": 6, "metric_value": 0.3333, "depth": 12}
												if obj[3]<=0:
													return 'True'
												elif obj[3]>0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[4]>5:
										# {"feature": "Passanger", "instances": 8, "metric_value": 0.3, "depth": 10}
										if obj[0]>1:
											# {"feature": "Direction_same", "instances": 5, "metric_value": 0.4, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Gender", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[3]<=0:
													return 'False'
												else: return 'False'
											elif obj[10]>0:
												return 'True'
											else: return 'True'
										elif obj[0]<=1:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[6]<=4:
									# {"feature": "Passanger", "instances": 35, "metric_value": 0.3966, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Gender", "instances": 22, "metric_value": 0.3209, "depth": 10}
										if obj[3]>0:
											# {"feature": "Age", "instances": 17, "metric_value": 0.3899, "depth": 11}
											if obj[4]>1:
												# {"feature": "Direction_same", "instances": 10, "metric_value": 0.2857, "depth": 12}
												if obj[10]>0:
													return 'False'
												elif obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[4]<=1:
												# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4048, "depth": 12}
												if obj[10]>0:
													return 'False'
												elif obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[3]<=0:
											return 'False'
										else: return 'False'
									elif obj[0]>1:
										# {"feature": "Age", "instances": 13, "metric_value": 0.2885, "depth": 10}
										if obj[4]>1:
											# {"feature": "Gender", "instances": 8, "metric_value": 0.375, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4, "depth": 12}
												if obj[10]<=0:
													return 'True'
												elif obj[10]>0:
													return 'False'
												else: return 'False'
											elif obj[3]<=0:
												return 'True'
											else: return 'True'
										elif obj[4]<=1:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[9]<=0.0:
								# {"feature": "Gender", "instances": 41, "metric_value": 0.3243, "depth": 8}
								if obj[3]>0:
									# {"feature": "Occupation", "instances": 23, "metric_value": 0.3399, "depth": 9}
									if obj[6]>5:
										# {"feature": "Passanger", "instances": 12, "metric_value": 0.4545, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Age", "instances": 11, "metric_value": 0.4545, "depth": 11}
											if obj[4]>0:
												# {"feature": "Direction_same", "instances": 10, "metric_value": 0.48, "depth": 12}
												if obj[10]<=0:
													return 'True'
												elif obj[10]>0:
													return 'False'
												else: return 'False'
											elif obj[4]<=0:
												return 'True'
											else: return 'True'
										elif obj[0]>1:
											return 'False'
										else: return 'False'
									elif obj[6]<=5:
										# {"feature": "Passanger", "instances": 11, "metric_value": 0.0, "depth": 10}
										if obj[0]<=1:
											return 'False'
										elif obj[0]>1:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[3]<=0:
									# {"feature": "Age", "instances": 18, "metric_value": 0.1046, "depth": 9}
									if obj[4]>1:
										# {"feature": "Occupation", "instances": 17, "metric_value": 0.1008, "depth": 10}
										if obj[6]>9:
											return 'False'
										elif obj[6]<=9:
											# {"feature": "Direction_same", "instances": 7, "metric_value": 0.2143, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Passanger", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[0]<=1:
													return 'False'
												else: return 'False'
											elif obj[10]>0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[4]<=1:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[8]>2.0:
						# {"feature": "Age", "instances": 84, "metric_value": 0.1841, "depth": 6}
						if obj[4]>0:
							# {"feature": "Occupation", "instances": 66, "metric_value": 0.131, "depth": 7}
							if obj[6]>6:
								# {"feature": "Gender", "instances": 37, "metric_value": 0.2185, "depth": 8}
								if obj[3]>0:
									# {"feature": "Time", "instances": 31, "metric_value": 0.1619, "depth": 9}
									if obj[1]>0:
										# {"feature": "Passanger", "instances": 22, "metric_value": 0.0606, "depth": 10}
										if obj[0]>0:
											return 'False'
										elif obj[0]<=0:
											# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[9]<=1.0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[1]<=0:
										# {"feature": "Passanger", "instances": 9, "metric_value": 0.3175, "depth": 10}
										if obj[0]>0:
											# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.381, "depth": 11}
											if obj[9]>-1.0:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'False'
												elif obj[10]>0:
													return 'False'
												else: return 'False'
											elif obj[9]<=-1.0:
												return 'False'
											else: return 'False'
										elif obj[0]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[3]<=0:
									# {"feature": "Passanger", "instances": 6, "metric_value": 0.4, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Time", "instances": 5, "metric_value": 0.4, "depth": 10}
										if obj[1]>0:
											# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.5, "depth": 11}
											if obj[9]<=1.0:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[1]<=0:
											return 'False'
										else: return 'False'
									elif obj[0]>1:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[6]<=6:
								return 'False'
							else: return 'False'
						elif obj[4]<=0:
							# {"feature": "Occupation", "instances": 18, "metric_value": 0.2685, "depth": 7}
							if obj[6]>1:
								# {"feature": "Time", "instances": 12, "metric_value": 0.125, "depth": 8}
								if obj[1]>0:
									return 'False'
								elif obj[1]<=0:
									# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.25, "depth": 9}
									if obj[9]<=1.0:
										# {"feature": "Passanger", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[0]<=2:
											# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[3]<=1:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=1:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[9]>1.0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[6]<=1:
								# {"feature": "Direction_same", "instances": 6, "metric_value": 0.25, "depth": 8}
								if obj[10]<=0:
									# {"feature": "Passanger", "instances": 4, "metric_value": 0.25, "depth": 9}
									if obj[0]>1:
										# {"feature": "Time", "instances": 2, "metric_value": 0.0, "depth": 10}
										if obj[1]<=0:
											return 'False'
										elif obj[1]>0:
											return 'True'
										else: return 'True'
									elif obj[0]<=1:
										return 'False'
									else: return 'False'
								elif obj[10]>0:
									return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[5]<=0:
					# {"feature": "Restaurant20to50", "instances": 281, "metric_value": 0.4271, "depth": 5}
					if obj[9]<=2.0:
						# {"feature": "Occupation", "instances": 267, "metric_value": 0.4247, "depth": 6}
						if obj[6]<=10:
							# {"feature": "Coffeehouse", "instances": 221, "metric_value": 0.4503, "depth": 7}
							if obj[8]>-1.0:
								# {"feature": "Age", "instances": 216, "metric_value": 0.4416, "depth": 8}
								if obj[4]>2:
									# {"feature": "Passanger", "instances": 151, "metric_value": 0.4758, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Time", "instances": 109, "metric_value": 0.4803, "depth": 10}
										if obj[1]<=2:
											# {"feature": "Direction_same", "instances": 76, "metric_value": 0.4672, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Gender", "instances": 45, "metric_value": 0.4876, "depth": 12}
												if obj[3]>0:
													return 'False'
												elif obj[3]<=0:
													return 'False'
												else: return 'False'
											elif obj[10]>0:
												# {"feature": "Gender", "instances": 31, "metric_value": 0.4369, "depth": 12}
												if obj[3]<=0:
													return 'False'
												elif obj[3]>0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[1]>2:
											# {"feature": "Direction_same", "instances": 33, "metric_value": 0.4893, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Gender", "instances": 27, "metric_value": 0.4663, "depth": 12}
												if obj[3]<=0:
													return 'False'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											elif obj[10]>0:
												# {"feature": "Gender", "instances": 6, "metric_value": 0.2222, "depth": 12}
												if obj[3]<=0:
													return 'True'
												elif obj[3]>0:
													return 'False'
												else: return 'False'
											else: return 'True'
										else: return 'True'
									elif obj[0]>1:
										# {"feature": "Gender", "instances": 42, "metric_value": 0.4259, "depth": 10}
										if obj[3]>0:
											# {"feature": "Time", "instances": 24, "metric_value": 0.3333, "depth": 11}
											if obj[1]>2:
												# {"feature": "Direction_same", "instances": 18, "metric_value": 0.2745, "depth": 12}
												if obj[10]<=0:
													return 'False'
												elif obj[10]>0:
													return 'False'
												else: return 'False'
											elif obj[1]<=2:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]<=0:
											# {"feature": "Time", "instances": 18, "metric_value": 0.4479, "depth": 11}
											if obj[1]>2:
												# {"feature": "Direction_same", "instances": 13, "metric_value": 0.497, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[1]<=2:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[4]<=2:
									# {"feature": "Gender", "instances": 65, "metric_value": 0.3443, "depth": 9}
									if obj[3]>0:
										# {"feature": "Passanger", "instances": 33, "metric_value": 0.4117, "depth": 10}
										if obj[0]>0:
											# {"feature": "Direction_same", "instances": 29, "metric_value": 0.3847, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Time", "instances": 22, "metric_value": 0.3209, "depth": 12}
												if obj[1]>1:
													return 'False'
												elif obj[1]<=1:
													return 'False'
												else: return 'False'
											elif obj[10]>0:
												# {"feature": "Time", "instances": 7, "metric_value": 0.4762, "depth": 12}
												if obj[1]>0:
													return 'True'
												elif obj[1]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[0]<=0:
											# {"feature": "Time", "instances": 4, "metric_value": 0.3333, "depth": 11}
											if obj[1]>0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[1]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[3]<=0:
										# {"feature": "Direction_same", "instances": 32, "metric_value": 0.25, "depth": 10}
										if obj[10]<=0:
											# {"feature": "Time", "instances": 25, "metric_value": 0.2947, "depth": 11}
											if obj[1]<=3:
												# {"feature": "Passanger", "instances": 19, "metric_value": 0.3715, "depth": 12}
												if obj[0]>0:
													return 'False'
												elif obj[0]<=0:
													return 'False'
												else: return 'False'
											elif obj[1]>3:
												return 'False'
											else: return 'False'
										elif obj[10]>0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[8]<=-1.0:
								# {"feature": "Gender", "instances": 5, "metric_value": 0.0, "depth": 8}
								if obj[3]<=0:
									return 'True'
								elif obj[3]>0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[6]>10:
							# {"feature": "Coffeehouse", "instances": 46, "metric_value": 0.2356, "depth": 7}
							if obj[8]>0.0:
								# {"feature": "Gender", "instances": 31, "metric_value": 0.2973, "depth": 8}
								if obj[3]>0:
									# {"feature": "Passanger", "instances": 23, "metric_value": 0.2116, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Time", "instances": 15, "metric_value": 0.1143, "depth": 10}
										if obj[1]>1:
											return 'False'
										elif obj[1]<=1:
											# {"feature": "Direction_same", "instances": 7, "metric_value": 0.1429, "depth": 11}
											if obj[10]>0:
												return 'False'
											elif obj[10]<=0:
												# {"feature": "Age", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[4]<=2:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[0]>1:
										# {"feature": "Age", "instances": 8, "metric_value": 0.3, "depth": 10}
										if obj[4]<=2:
											# {"feature": "Time", "instances": 5, "metric_value": 0.4667, "depth": 11}
											if obj[1]>2:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[1]<=2:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[4]>2:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[3]<=0:
									# {"feature": "Age", "instances": 8, "metric_value": 0.375, "depth": 9}
									if obj[4]<=2:
										# {"feature": "Passanger", "instances": 4, "metric_value": 0.25, "depth": 10}
										if obj[0]>0:
											return 'True'
										elif obj[0]<=0:
											# {"feature": "Time", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[1]<=4:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[4]>2:
										# {"feature": "Passanger", "instances": 4, "metric_value": 0.25, "depth": 10}
										if obj[0]>0:
											return 'False'
										elif obj[0]<=0:
											# {"feature": "Time", "instances": 2, "metric_value": 0.0, "depth": 11}
											if obj[1]>0:
												return 'True'
											elif obj[1]<=0:
												return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'False'
								else: return 'True'
							elif obj[8]<=0.0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[9]>2.0:
						# {"feature": "Coffeehouse", "instances": 14, "metric_value": 0.1714, "depth": 6}
						if obj[8]<=2.0:
							return 'True'
						elif obj[8]>2.0:
							# {"feature": "Passanger", "instances": 5, "metric_value": 0.2667, "depth": 7}
							if obj[0]<=2:
								# {"feature": "Direction_same", "instances": 3, "metric_value": 0.0, "depth": 8}
								if obj[10]<=0:
									return 'False'
								elif obj[10]>0:
									return 'True'
								else: return 'True'
							elif obj[0]>2:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[11]>2:
				# {"feature": "Education", "instances": 178, "metric_value": 0.2796, "depth": 4}
				if obj[5]<=4:
					# {"feature": "Occupation", "instances": 176, "metric_value": 0.2721, "depth": 5}
					if obj[6]<=11.790657263862823:
						# {"feature": "Gender", "instances": 150, "metric_value": 0.2271, "depth": 6}
						if obj[3]>0:
							# {"feature": "Coffeehouse", "instances": 80, "metric_value": 0.1148, "depth": 7}
							if obj[8]>1.0:
								# {"feature": "Restaurant20to50", "instances": 42, "metric_value": 0.1673, "depth": 8}
								if obj[9]>0.0:
									# {"feature": "Time", "instances": 38, "metric_value": 0.1421, "depth": 9}
									if obj[1]>0:
										# {"feature": "Age", "instances": 30, "metric_value": 0.1731, "depth": 10}
										if obj[4]<=5:
											# {"feature": "Passanger", "instances": 26, "metric_value": 0.1399, "depth": 11}
											if obj[0]>0:
												# {"feature": "Direction_same", "instances": 22, "metric_value": 0.1653, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[0]<=0:
												return 'False'
											else: return 'False'
										elif obj[4]>5:
											# {"feature": "Passanger", "instances": 4, "metric_value": 0.375, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[1]<=0:
										return 'False'
									else: return 'False'
								elif obj[9]<=0.0:
									# {"feature": "Age", "instances": 4, "metric_value": 0.25, "depth": 9}
									if obj[4]>3:
										# {"feature": "Passanger", "instances": 2, "metric_value": 0.0, "depth": 10}
										if obj[0]>0:
											return 'True'
										elif obj[0]<=0:
											return 'False'
										else: return 'False'
									elif obj[4]<=3:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[8]<=1.0:
								# {"feature": "Restaurant20to50", "instances": 38, "metric_value": 0.0478, "depth": 8}
								if obj[9]>0.0:
									return 'False'
								elif obj[9]<=0.0:
									# {"feature": "Age", "instances": 11, "metric_value": 0.1364, "depth": 9}
									if obj[4]<=2:
										return 'False'
									elif obj[4]>2:
										# {"feature": "Time", "instances": 4, "metric_value": 0.3333, "depth": 10}
										if obj[1]>0:
											# {"feature": "Passanger", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[1]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[3]<=0:
							# {"feature": "Passanger", "instances": 70, "metric_value": 0.3354, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Age", "instances": 69, "metric_value": 0.3313, "depth": 8}
								if obj[4]<=6:
									# {"feature": "Time", "instances": 63, "metric_value": 0.3551, "depth": 9}
									if obj[1]<=1:
										# {"feature": "Restaurant20to50", "instances": 59, "metric_value": 0.3747, "depth": 10}
										if obj[9]>-1.0:
											# {"feature": "Coffeehouse", "instances": 57, "metric_value": 0.3837, "depth": 11}
											if obj[8]<=3.0:
												# {"feature": "Direction_same", "instances": 55, "metric_value": 0.3795, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[8]>3.0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[9]<=-1.0:
											return 'False'
										else: return 'False'
									elif obj[1]>1:
										return 'False'
									else: return 'False'
								elif obj[4]>6:
									return 'False'
								else: return 'False'
							elif obj[0]>1:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[6]>11.790657263862823:
						# {"feature": "Restaurant20to50", "instances": 26, "metric_value": 0.3814, "depth": 6}
						if obj[9]<=2.0:
							# {"feature": "Age", "instances": 24, "metric_value": 0.3792, "depth": 7}
							if obj[4]<=4:
								# {"feature": "Passanger", "instances": 20, "metric_value": 0.4105, "depth": 8}
								if obj[0]<=1:
									# {"feature": "Coffeehouse", "instances": 19, "metric_value": 0.4008, "depth": 9}
									if obj[8]>0.0:
										# {"feature": "Time", "instances": 13, "metric_value": 0.3462, "depth": 10}
										if obj[1]>0:
											# {"feature": "Gender", "instances": 12, "metric_value": 0.3704, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 9, "metric_value": 0.3457, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[1]<=0:
											return 'False'
										else: return 'False'
									elif obj[8]<=0.0:
										# {"feature": "Time", "instances": 6, "metric_value": 0.5, "depth": 10}
										if obj[1]<=1:
											# {"feature": "Gender", "instances": 6, "metric_value": 0.5, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[0]>1:
									return 'True'
								else: return 'True'
							elif obj[4]>4:
								return 'False'
							else: return 'False'
						elif obj[9]>2.0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[5]>4:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'False'
	else: return 'False'
