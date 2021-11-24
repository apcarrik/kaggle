def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Coupon", "instances": 8147, "metric_value": 0.4744, "depth": 1}
	if obj[2]>1:
		# {"feature": "Coffeehouse", "instances": 5889, "metric_value": 0.4587, "depth": 2}
		if obj[9]>0.0:
			# {"feature": "Distance", "instances": 4432, "metric_value": 0.4358, "depth": 3}
			if obj[12]<=2:
				# {"feature": "Passanger", "instances": 4015, "metric_value": 0.4266, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Time", "instances": 2626, "metric_value": 0.4479, "depth": 5}
					if obj[1]<=3:
						# {"feature": "Occupation", "instances": 2123, "metric_value": 0.4553, "depth": 6}
						if obj[7]>0:
							# {"feature": "Gender", "instances": 2109, "metric_value": 0.4564, "depth": 7}
							if obj[3]>0:
								# {"feature": "Bar", "instances": 1135, "metric_value": 0.4662, "depth": 8}
								if obj[8]<=3.0:
									# {"feature": "Education", "instances": 1105, "metric_value": 0.4644, "depth": 9}
									if obj[6]<=2:
										# {"feature": "Direction_same", "instances": 830, "metric_value": 0.455, "depth": 10}
										if obj[11]<=0:
											# {"feature": "Restaurant20to50", "instances": 476, "metric_value": 0.4704, "depth": 11}
											if obj[10]<=3.0:
												# {"feature": "Children", "instances": 467, "metric_value": 0.4735, "depth": 12}
												if obj[5]>0:
													# {"feature": "Age", "instances": 261, "metric_value": 0.4576, "depth": 13}
													if obj[4]<=3:
														return 'True'
													elif obj[4]>3:
														return 'True'
													else: return 'True'
												elif obj[5]<=0:
													# {"feature": "Age", "instances": 206, "metric_value": 0.4864, "depth": 13}
													if obj[4]<=2:
														return 'True'
													elif obj[4]>2:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[10]>3.0:
												# {"feature": "Age", "instances": 9, "metric_value": 0.1852, "depth": 12}
												if obj[4]>0:
													# {"feature": "Children", "instances": 6, "metric_value": 0.2778, "depth": 13}
													if obj[5]<=0:
														return 'True'
													else: return 'True'
												elif obj[4]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[11]>0:
											# {"feature": "Age", "instances": 354, "metric_value": 0.4287, "depth": 11}
											if obj[4]<=4:
												# {"feature": "Restaurant20to50", "instances": 302, "metric_value": 0.4203, "depth": 12}
												if obj[10]>0.0:
													# {"feature": "Children", "instances": 259, "metric_value": 0.4124, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												elif obj[10]<=0.0:
													# {"feature": "Children", "instances": 43, "metric_value": 0.4296, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[4]>4:
												# {"feature": "Restaurant20to50", "instances": 52, "metric_value": 0.4491, "depth": 12}
												if obj[10]<=1.0:
													# {"feature": "Children", "instances": 29, "metric_value": 0.4946, "depth": 13}
													if obj[5]>0:
														return 'True'
													elif obj[5]<=0:
														return 'False'
													else: return 'False'
												elif obj[10]>1.0:
													# {"feature": "Children", "instances": 23, "metric_value": 0.3851, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[6]>2:
										# {"feature": "Age", "instances": 275, "metric_value": 0.4776, "depth": 10}
										if obj[4]<=2:
											# {"feature": "Restaurant20to50", "instances": 163, "metric_value": 0.4916, "depth": 11}
											if obj[10]<=1.0:
												# {"feature": "Children", "instances": 100, "metric_value": 0.498, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 52, "metric_value": 0.4949, "depth": 13}
													if obj[11]>0:
														return 'False'
													elif obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 48, "metric_value": 0.4991, "depth": 13}
													if obj[11]>0:
														return 'True'
													elif obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[10]>1.0:
												# {"feature": "Children", "instances": 63, "metric_value": 0.4739, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 47, "metric_value": 0.4807, "depth": 13}
													if obj[11]>0:
														return 'True'
													elif obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 16, "metric_value": 0.4286, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[4]>2:
											# {"feature": "Restaurant20to50", "instances": 112, "metric_value": 0.4341, "depth": 11}
											if obj[10]<=1.0:
												# {"feature": "Children", "instances": 75, "metric_value": 0.3953, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 44, "metric_value": 0.3393, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[5]<=0:
													# {"feature": "Direction_same", "instances": 31, "metric_value": 0.4578, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[10]>1.0:
												# {"feature": "Children", "instances": 37, "metric_value": 0.4725, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 29, "metric_value": 0.4932, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												elif obj[5]<=0:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.3667, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[8]>3.0:
									# {"feature": "Age", "instances": 30, "metric_value": 0.3909, "depth": 9}
									if obj[4]<=4:
										# {"feature": "Education", "instances": 22, "metric_value": 0.3636, "depth": 10}
										if obj[6]<=2:
											# {"feature": "Direction_same", "instances": 18, "metric_value": 0.4198, "depth": 11}
											if obj[11]>0:
												# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.3333, "depth": 12}
												if obj[10]<=0.0:
													# {"feature": "Children", "instances": 6, "metric_value": 0.2778, "depth": 13}
													if obj[5]<=0:
														return 'False'
													else: return 'False'
												elif obj[10]>0.0:
													# {"feature": "Children", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[5]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[11]<=0:
												# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.4333, "depth": 12}
												if obj[10]<=0.0:
													# {"feature": "Children", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[5]<=0:
														return 'True'
													else: return 'True'
												elif obj[10]>0.0:
													# {"feature": "Children", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[5]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[6]>2:
											return 'False'
										else: return 'False'
									elif obj[4]>4:
										# {"feature": "Direction_same", "instances": 8, "metric_value": 0.3, "depth": 10}
										if obj[11]<=0:
											# {"feature": "Children", "instances": 5, "metric_value": 0.48, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Education", "instances": 5, "metric_value": 0.48, "depth": 12}
												if obj[6]<=2:
													# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[10]<=4.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[11]>0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[3]<=0:
								# {"feature": "Bar", "instances": 974, "metric_value": 0.4405, "depth": 8}
								if obj[8]>-1.0:
									# {"feature": "Direction_same", "instances": 968, "metric_value": 0.4391, "depth": 9}
									if obj[11]<=0:
										# {"feature": "Age", "instances": 526, "metric_value": 0.4528, "depth": 10}
										if obj[4]>0:
											# {"feature": "Education", "instances": 458, "metric_value": 0.445, "depth": 11}
											if obj[6]>0:
												# {"feature": "Restaurant20to50", "instances": 291, "metric_value": 0.432, "depth": 12}
												if obj[10]<=3.0:
													# {"feature": "Children", "instances": 279, "metric_value": 0.4342, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												elif obj[10]>3.0:
													# {"feature": "Children", "instances": 12, "metric_value": 0.3714, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[6]<=0:
												# {"feature": "Restaurant20to50", "instances": 167, "metric_value": 0.4573, "depth": 12}
												if obj[10]<=1.0:
													# {"feature": "Children", "instances": 112, "metric_value": 0.4869, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												elif obj[10]>1.0:
													# {"feature": "Children", "instances": 55, "metric_value": 0.3965, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[4]<=0:
											# {"feature": "Restaurant20to50", "instances": 68, "metric_value": 0.4799, "depth": 11}
											if obj[10]<=3.0:
												# {"feature": "Education", "instances": 62, "metric_value": 0.4886, "depth": 12}
												if obj[6]>0:
													# {"feature": "Children", "instances": 41, "metric_value": 0.497, "depth": 13}
													if obj[5]<=0:
														return 'False'
													elif obj[5]>0:
														return 'False'
													else: return 'False'
												elif obj[6]<=0:
													# {"feature": "Children", "instances": 21, "metric_value": 0.4259, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'False'
													else: return 'False'
												else: return 'True'
											elif obj[10]>3.0:
												# {"feature": "Children", "instances": 6, "metric_value": 0.2222, "depth": 12}
												if obj[5]>0:
													# {"feature": "Education", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[6]<=4:
														return 'True'
													else: return 'True'
												elif obj[5]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[11]>0:
										# {"feature": "Restaurant20to50", "instances": 442, "metric_value": 0.4156, "depth": 10}
										if obj[10]<=2.0:
											# {"feature": "Age", "instances": 393, "metric_value": 0.4281, "depth": 11}
											if obj[4]<=4:
												# {"feature": "Education", "instances": 293, "metric_value": 0.4409, "depth": 12}
												if obj[6]<=3:
													# {"feature": "Children", "instances": 274, "metric_value": 0.4458, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												elif obj[6]>3:
													# {"feature": "Children", "instances": 19, "metric_value": 0.3268, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[4]>4:
												# {"feature": "Education", "instances": 100, "metric_value": 0.3775, "depth": 12}
												if obj[6]<=2:
													# {"feature": "Children", "instances": 79, "metric_value": 0.4119, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												elif obj[6]>2:
													# {"feature": "Children", "instances": 21, "metric_value": 0.2445, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[10]>2.0:
											# {"feature": "Age", "instances": 49, "metric_value": 0.2704, "depth": 11}
											if obj[4]>1:
												# {"feature": "Education", "instances": 27, "metric_value": 0.1323, "depth": 12}
												if obj[6]<=3:
													# {"feature": "Children", "instances": 21, "metric_value": 0.0896, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												elif obj[6]>3:
													# {"feature": "Children", "instances": 6, "metric_value": 0.2222, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[4]<=1:
												# {"feature": "Education", "instances": 22, "metric_value": 0.3955, "depth": 12}
												if obj[6]>0:
													# {"feature": "Children", "instances": 19, "metric_value": 0.3709, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												elif obj[6]<=0:
													# {"feature": "Children", "instances": 3, "metric_value": 0.3333, "depth": 13}
													if obj[5]>0:
														return 'True'
													elif obj[5]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[8]<=-1.0:
									# {"feature": "Direction_same", "instances": 6, "metric_value": 0.2222, "depth": 9}
									if obj[11]<=0:
										# {"feature": "Age", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[4]<=3:
											# {"feature": "Children", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[5]<=1:
												# {"feature": "Education", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[6]<=2:
													# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[10]<=2.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[11]>0:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[7]<=0:
							# {"feature": "Age", "instances": 14, "metric_value": 0.1143, "depth": 7}
							if obj[4]<=6:
								return 'True'
							elif obj[4]>6:
								# {"feature": "Direction_same", "instances": 5, "metric_value": 0.2667, "depth": 8}
								if obj[11]<=0:
									# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 9}
									if obj[3]<=1:
										# {"feature": "Children", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Education", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[6]<=2:
												# {"feature": "Bar", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[8]<=2.0:
													# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[10]<=1.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[11]>0:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[1]>3:
						# {"feature": "Bar", "instances": 503, "metric_value": 0.4078, "depth": 6}
						if obj[8]<=1.0:
							# {"feature": "Occupation", "instances": 337, "metric_value": 0.3791, "depth": 7}
							if obj[7]<=13.168241765136806:
								# {"feature": "Children", "instances": 281, "metric_value": 0.359, "depth": 8}
								if obj[5]>0:
									# {"feature": "Age", "instances": 141, "metric_value": 0.3976, "depth": 9}
									if obj[4]<=4:
										# {"feature": "Education", "instances": 109, "metric_value": 0.368, "depth": 10}
										if obj[6]<=3:
											# {"feature": "Restaurant20to50", "instances": 105, "metric_value": 0.3812, "depth": 11}
											if obj[10]<=1.0:
												# {"feature": "Gender", "instances": 70, "metric_value": 0.3953, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 49, "metric_value": 0.3898, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 21, "metric_value": 0.4082, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[10]>1.0:
												# {"feature": "Gender", "instances": 35, "metric_value": 0.3524, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 30, "metric_value": 0.3578, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[6]>3:
											return 'True'
										else: return 'True'
									elif obj[4]>4:
										# {"feature": "Gender", "instances": 32, "metric_value": 0.4297, "depth": 10}
										if obj[3]>0:
											# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.3274, "depth": 11}
											if obj[10]>0.0:
												# {"feature": "Education", "instances": 16, "metric_value": 0.3545, "depth": 12}
												if obj[6]>0:
													# {"feature": "Direction_same", "instances": 11, "metric_value": 0.2975, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[6]<=0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[10]<=0.0:
												return 'True'
											else: return 'True'
										elif obj[3]<=0:
											# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.1636, "depth": 11}
											if obj[10]>0.0:
												# {"feature": "Education", "instances": 10, "metric_value": 0.1667, "depth": 12}
												if obj[6]<=1:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.2778, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[6]>1:
													return 'True'
												else: return 'True'
											elif obj[10]<=0.0:
												return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'True'
								elif obj[5]<=0:
									# {"feature": "Age", "instances": 140, "metric_value": 0.3009, "depth": 9}
									if obj[4]<=4:
										# {"feature": "Education", "instances": 101, "metric_value": 0.3554, "depth": 10}
										if obj[6]<=2:
											# {"feature": "Restaurant20to50", "instances": 83, "metric_value": 0.3818, "depth": 11}
											if obj[10]>0.0:
												# {"feature": "Gender", "instances": 71, "metric_value": 0.364, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 36, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 35, "metric_value": 0.3527, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[10]<=0.0:
												# {"feature": "Gender", "instances": 12, "metric_value": 0.4857, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4898, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[6]>2:
											# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.1597, "depth": 11}
											if obj[10]<=2.0:
												# {"feature": "Gender", "instances": 16, "metric_value": 0.1094, "depth": 12}
												if obj[3]>0:
													return 'True'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.2188, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[10]>2.0:
												# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[4]>4:
										# {"feature": "Gender", "instances": 39, "metric_value": 0.1346, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Education", "instances": 24, "metric_value": 0.2031, "depth": 11}
											if obj[6]<=0:
												# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.1154, "depth": 12}
												if obj[10]>0.0:
													# {"feature": "Direction_same", "instances": 13, "metric_value": 0.142, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[10]<=0.0:
													return 'True'
												else: return 'True'
											elif obj[6]>0:
												# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.3571, "depth": 12}
												if obj[10]>0.0:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4082, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[10]<=0.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]>0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[7]>13.168241765136806:
								# {"feature": "Age", "instances": 56, "metric_value": 0.4396, "depth": 8}
								if obj[4]<=6:
									# {"feature": "Education", "instances": 52, "metric_value": 0.4497, "depth": 9}
									if obj[6]<=2:
										# {"feature": "Children", "instances": 40, "metric_value": 0.4221, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.3079, "depth": 11}
											if obj[10]<=1.0:
												# {"feature": "Gender", "instances": 15, "metric_value": 0.2074, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 9, "metric_value": 0.3457, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											elif obj[10]>1.0:
												# {"feature": "Gender", "instances": 6, "metric_value": 0.25, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[5]>0:
											# {"feature": "Restaurant20to50", "instances": 19, "metric_value": 0.393, "depth": 11}
											if obj[10]<=1.0:
												# {"feature": "Gender", "instances": 15, "metric_value": 0.4571, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 14, "metric_value": 0.4898, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											elif obj[10]>1.0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[6]>2:
										# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.4583, "depth": 10}
										if obj[10]<=1.0:
											# {"feature": "Gender", "instances": 8, "metric_value": 0.5, "depth": 11}
											if obj[3]>0:
												# {"feature": "Children", "instances": 6, "metric_value": 0.4, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[5]>0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Children", "instances": 2, "metric_value": 0.0, "depth": 12}
												if obj[5]<=0:
													return 'True'
												elif obj[5]>0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[10]>1.0:
											# {"feature": "Gender", "instances": 4, "metric_value": 0.3333, "depth": 11}
											if obj[3]>0:
												# {"feature": "Children", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[3]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[4]>6:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[8]>1.0:
							# {"feature": "Education", "instances": 166, "metric_value": 0.4524, "depth": 7}
							if obj[6]>0:
								# {"feature": "Occupation", "instances": 115, "metric_value": 0.4565, "depth": 8}
								if obj[7]<=19:
									# {"feature": "Age", "instances": 112, "metric_value": 0.4581, "depth": 9}
									if obj[4]<=3:
										# {"feature": "Restaurant20to50", "instances": 78, "metric_value": 0.4844, "depth": 10}
										if obj[10]<=3.0:
											# {"feature": "Gender", "instances": 71, "metric_value": 0.4908, "depth": 11}
											if obj[3]>0:
												# {"feature": "Children", "instances": 37, "metric_value": 0.4814, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 25, "metric_value": 0.4992, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 12, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Children", "instances": 34, "metric_value": 0.4747, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 19, "metric_value": 0.4986, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]<=0:
													# {"feature": "Direction_same", "instances": 15, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[10]>3.0:
											# {"feature": "Children", "instances": 7, "metric_value": 0.3429, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Gender", "instances": 5, "metric_value": 0.48, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[5]>0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[4]>3:
										# {"feature": "Restaurant20to50", "instances": 34, "metric_value": 0.3737, "depth": 10}
										if obj[10]<=1.0:
											# {"feature": "Gender", "instances": 17, "metric_value": 0.2017, "depth": 11}
											if obj[3]<=0:
												return 'True'
											elif obj[3]>0:
												# {"feature": "Children", "instances": 7, "metric_value": 0.4898, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4898, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[10]>1.0:
											# {"feature": "Gender", "instances": 17, "metric_value": 0.395, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Children", "instances": 10, "metric_value": 0.5, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Children", "instances": 7, "metric_value": 0.1429, "depth": 12}
												if obj[5]<=0:
													return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[7]>19:
									return 'False'
								else: return 'False'
							elif obj[6]<=0:
								# {"feature": "Occupation", "instances": 51, "metric_value": 0.3037, "depth": 8}
								if obj[7]>4:
									# {"feature": "Restaurant20to50", "instances": 39, "metric_value": 0.2501, "depth": 9}
									if obj[10]<=1.0:
										# {"feature": "Age", "instances": 22, "metric_value": 0.154, "depth": 10}
										if obj[4]<=4:
											# {"feature": "Children", "instances": 18, "metric_value": 0.0972, "depth": 11}
											if obj[5]<=0:
												return 'True'
											elif obj[5]>0:
												# {"feature": "Gender", "instances": 8, "metric_value": 0.2, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[4]>4:
											# {"feature": "Children", "instances": 4, "metric_value": 0.3333, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[5]>0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[10]>1.0:
										# {"feature": "Age", "instances": 17, "metric_value": 0.3167, "depth": 10}
										if obj[4]>0:
											# {"feature": "Children", "instances": 13, "metric_value": 0.2393, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Gender", "instances": 9, "metric_value": 0.3444, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[5]>0:
												return 'True'
											else: return 'True'
										elif obj[4]<=0:
											# {"feature": "Children", "instances": 4, "metric_value": 0.3333, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[5]>0:
												return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'True'
								elif obj[7]<=4:
									# {"feature": "Age", "instances": 12, "metric_value": 0.3636, "depth": 9}
									if obj[4]>0:
										# {"feature": "Gender", "instances": 11, "metric_value": 0.3117, "depth": 10}
										if obj[3]>0:
											# {"feature": "Children", "instances": 7, "metric_value": 0.3429, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.3, "depth": 12}
												if obj[10]<=1.0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[10]>1.0:
													return 'False'
												else: return 'False'
											elif obj[5]>0:
												return 'False'
											else: return 'False'
										elif obj[3]<=0:
											return 'False'
										else: return 'False'
									elif obj[4]<=0:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[0]>2:
					# {"feature": "Occupation", "instances": 1389, "metric_value": 0.382, "depth": 5}
					if obj[7]<=18.52567473260329:
						# {"feature": "Bar", "instances": 1292, "metric_value": 0.3906, "depth": 6}
						if obj[8]<=3.0:
							# {"feature": "Children", "instances": 1225, "metric_value": 0.3841, "depth": 7}
							if obj[5]<=0:
								# {"feature": "Age", "instances": 741, "metric_value": 0.3583, "depth": 8}
								if obj[4]<=4:
									# {"feature": "Restaurant20to50", "instances": 615, "metric_value": 0.3747, "depth": 9}
									if obj[10]<=2.0:
										# {"feature": "Time", "instances": 580, "metric_value": 0.3829, "depth": 10}
										if obj[1]<=2:
											# {"feature": "Education", "instances": 366, "metric_value": 0.3556, "depth": 11}
											if obj[6]>0:
												# {"feature": "Gender", "instances": 233, "metric_value": 0.322, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 123, "metric_value": 0.3141, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 110, "metric_value": 0.3307, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[6]<=0:
												# {"feature": "Gender", "instances": 133, "metric_value": 0.4116, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 70, "metric_value": 0.382, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 63, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[1]>2:
											# {"feature": "Education", "instances": 214, "metric_value": 0.4152, "depth": 11}
											if obj[6]<=2:
												# {"feature": "Gender", "instances": 175, "metric_value": 0.3936, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 88, "metric_value": 0.3512, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 87, "metric_value": 0.4365, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[6]>2:
												# {"feature": "Gender", "instances": 39, "metric_value": 0.4909, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 22, "metric_value": 0.4959, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 17, "metric_value": 0.4844, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[10]>2.0:
										# {"feature": "Time", "instances": 35, "metric_value": 0.187, "depth": 10}
										if obj[1]<=2:
											# {"feature": "Education", "instances": 22, "metric_value": 0.2864, "depth": 11}
											if obj[6]>1:
												# {"feature": "Gender", "instances": 12, "metric_value": 0.3704, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 9, "metric_value": 0.3457, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[6]<=1:
												# {"feature": "Gender", "instances": 10, "metric_value": 0.18, "depth": 12}
												if obj[3]<=1:
													# {"feature": "Direction_same", "instances": 10, "metric_value": 0.18, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[1]>2:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[4]>4:
									# {"feature": "Education", "instances": 126, "metric_value": 0.2636, "depth": 9}
									if obj[6]<=1:
										# {"feature": "Restaurant20to50", "instances": 73, "metric_value": 0.2082, "depth": 10}
										if obj[10]<=1.0:
											# {"feature": "Time", "instances": 47, "metric_value": 0.2699, "depth": 11}
											if obj[1]>0:
												# {"feature": "Gender", "instances": 38, "metric_value": 0.2211, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 30, "metric_value": 0.18, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[1]<=0:
												# {"feature": "Gender", "instances": 9, "metric_value": 0.3333, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[10]>1.0:
											# {"feature": "Time", "instances": 26, "metric_value": 0.0659, "depth": 11}
											if obj[1]<=3:
												return 'True'
											elif obj[1]>3:
												# {"feature": "Gender", "instances": 7, "metric_value": 0.2143, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[6]>1:
										# {"feature": "Gender", "instances": 53, "metric_value": 0.3172, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Time", "instances": 34, "metric_value": 0.3816, "depth": 11}
											if obj[1]>0:
												# {"feature": "Restaurant20to50", "instances": 27, "metric_value": 0.409, "depth": 12}
												if obj[10]>1.0:
													# {"feature": "Direction_same", "instances": 14, "metric_value": 0.4592, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[10]<=1.0:
													# {"feature": "Direction_same", "instances": 13, "metric_value": 0.355, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[1]<=0:
												# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.2286, "depth": 12}
												if obj[10]>1.0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[10]<=1.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]>0:
											# {"feature": "Restaurant20to50", "instances": 19, "metric_value": 0.1579, "depth": 11}
											if obj[10]>0.0:
												return 'True'
											elif obj[10]<=0.0:
												# {"feature": "Time", "instances": 8, "metric_value": 0.3333, "depth": 12}
												if obj[1]>0:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.2778, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[1]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[5]>0:
								# {"feature": "Restaurant20to50", "instances": 484, "metric_value": 0.4102, "depth": 8}
								if obj[10]<=1.0:
									# {"feature": "Age", "instances": 314, "metric_value": 0.4512, "depth": 9}
									if obj[4]>1:
										# {"feature": "Gender", "instances": 243, "metric_value": 0.4595, "depth": 10}
										if obj[3]>0:
											# {"feature": "Time", "instances": 161, "metric_value": 0.4855, "depth": 11}
											if obj[1]>0:
												# {"feature": "Education", "instances": 124, "metric_value": 0.4774, "depth": 12}
												if obj[6]<=2:
													# {"feature": "Direction_same", "instances": 95, "metric_value": 0.4707, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[6]>2:
													# {"feature": "Direction_same", "instances": 29, "metric_value": 0.4994, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[1]<=0:
												# {"feature": "Education", "instances": 37, "metric_value": 0.465, "depth": 12}
												if obj[6]<=2:
													# {"feature": "Direction_same", "instances": 24, "metric_value": 0.4861, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[6]>2:
													# {"feature": "Direction_same", "instances": 13, "metric_value": 0.426, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]<=0:
											# {"feature": "Time", "instances": 82, "metric_value": 0.3947, "depth": 11}
											if obj[1]<=2:
												# {"feature": "Education", "instances": 55, "metric_value": 0.4368, "depth": 12}
												if obj[6]<=2:
													# {"feature": "Direction_same", "instances": 34, "metric_value": 0.4152, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[6]>2:
													# {"feature": "Direction_same", "instances": 21, "metric_value": 0.4717, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[1]>2:
												# {"feature": "Education", "instances": 27, "metric_value": 0.2346, "depth": 12}
												if obj[6]>0:
													# {"feature": "Direction_same", "instances": 18, "metric_value": 0.1049, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[6]<=0:
													# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4938, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[4]<=1:
										# {"feature": "Gender", "instances": 71, "metric_value": 0.3748, "depth": 10}
										if obj[3]>0:
											# {"feature": "Education", "instances": 52, "metric_value": 0.294, "depth": 11}
											if obj[6]<=2:
												# {"feature": "Time", "instances": 42, "metric_value": 0.2424, "depth": 12}
												if obj[1]<=2:
													# {"feature": "Direction_same", "instances": 26, "metric_value": 0.2041, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[1]>2:
													# {"feature": "Direction_same", "instances": 16, "metric_value": 0.3047, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[6]>2:
												# {"feature": "Time", "instances": 10, "metric_value": 0.375, "depth": 12}
												if obj[1]>0:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.4688, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[1]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]<=0:
											# {"feature": "Education", "instances": 19, "metric_value": 0.3306, "depth": 11}
											if obj[6]>1:
												# {"feature": "Time", "instances": 13, "metric_value": 0.3231, "depth": 12}
												if obj[1]>0:
													# {"feature": "Direction_same", "instances": 10, "metric_value": 0.42, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[1]<=0:
													return 'True'
												else: return 'True'
											elif obj[6]<=1:
												# {"feature": "Time", "instances": 6, "metric_value": 0.2222, "depth": 12}
												if obj[1]>2:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[1]<=2:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'True'
								elif obj[10]>1.0:
									# {"feature": "Age", "instances": 170, "metric_value": 0.3155, "depth": 9}
									if obj[4]>0:
										# {"feature": "Time", "instances": 144, "metric_value": 0.2843, "depth": 10}
										if obj[1]<=2:
											# {"feature": "Gender", "instances": 83, "metric_value": 0.3189, "depth": 11}
											if obj[3]>0:
												# {"feature": "Education", "instances": 52, "metric_value": 0.372, "depth": 12}
												if obj[6]>1:
													# {"feature": "Direction_same", "instances": 28, "metric_value": 0.3367, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[6]<=1:
													# {"feature": "Direction_same", "instances": 24, "metric_value": 0.4132, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Education", "instances": 31, "metric_value": 0.2153, "depth": 12}
												if obj[6]<=1:
													# {"feature": "Direction_same", "instances": 16, "metric_value": 0.1172, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[6]>1:
													# {"feature": "Direction_same", "instances": 15, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[1]>2:
											# {"feature": "Education", "instances": 61, "metric_value": 0.2179, "depth": 11}
											if obj[6]<=2:
												# {"feature": "Gender", "instances": 45, "metric_value": 0.16, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 30, "metric_value": 0.1244, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 15, "metric_value": 0.2311, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[6]>2:
												# {"feature": "Gender", "instances": 16, "metric_value": 0.3438, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.4688, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.2188, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[4]<=0:
										# {"feature": "Time", "instances": 26, "metric_value": 0.3469, "depth": 10}
										if obj[1]>2:
											# {"feature": "Education", "instances": 15, "metric_value": 0.3692, "depth": 11}
											if obj[6]<=3:
												# {"feature": "Gender", "instances": 13, "metric_value": 0.3487, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 10, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[6]>3:
												return 'True'
											else: return 'True'
										elif obj[1]<=2:
											# {"feature": "Education", "instances": 11, "metric_value": 0.1364, "depth": 11}
											if obj[6]>2:
												return 'True'
											elif obj[6]<=2:
												# {"feature": "Gender", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[3]<=1:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[8]>3.0:
							# {"feature": "Time", "instances": 67, "metric_value": 0.4397, "depth": 7}
							if obj[1]>0:
								# {"feature": "Children", "instances": 51, "metric_value": 0.4044, "depth": 8}
								if obj[5]<=0:
									# {"feature": "Restaurant20to50", "instances": 45, "metric_value": 0.3978, "depth": 9}
									if obj[10]<=2.0:
										# {"feature": "Education", "instances": 25, "metric_value": 0.3, "depth": 10}
										if obj[6]<=0:
											# {"feature": "Gender", "instances": 16, "metric_value": 0.1944, "depth": 11}
											if obj[3]>0:
												# {"feature": "Age", "instances": 9, "metric_value": 0.3457, "depth": 12}
												if obj[4]<=4:
													# {"feature": "Direction_same", "instances": 9, "metric_value": 0.3457, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]<=0:
												return 'True'
											else: return 'True'
										elif obj[6]>0:
											# {"feature": "Gender", "instances": 9, "metric_value": 0.3333, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Age", "instances": 6, "metric_value": 0.5, "depth": 12}
												if obj[4]<=4:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[3]>0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[10]>2.0:
										# {"feature": "Gender", "instances": 20, "metric_value": 0.4235, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Education", "instances": 17, "metric_value": 0.4973, "depth": 11}
											if obj[6]>0:
												# {"feature": "Age", "instances": 11, "metric_value": 0.4959, "depth": 12}
												if obj[4]<=1:
													# {"feature": "Direction_same", "instances": 11, "metric_value": 0.4959, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[6]<=0:
												# {"feature": "Age", "instances": 6, "metric_value": 0.5, "depth": 12}
												if obj[4]<=1:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[3]>0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[5]>0:
									return 'True'
								else: return 'True'
							elif obj[1]<=0:
								# {"feature": "Age", "instances": 16, "metric_value": 0.4167, "depth": 8}
								if obj[4]<=4:
									# {"feature": "Children", "instances": 15, "metric_value": 0.381, "depth": 9}
									if obj[5]<=0:
										# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.3673, "depth": 10}
										if obj[10]>2.0:
											# {"feature": "Education", "instances": 7, "metric_value": 0.2143, "depth": 11}
											if obj[6]>3:
												# {"feature": "Gender", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[6]<=3:
												return 'False'
											else: return 'False'
										elif obj[10]<=2.0:
											# {"feature": "Gender", "instances": 7, "metric_value": 0.4762, "depth": 11}
											if obj[3]>0:
												# {"feature": "Education", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[6]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[6]>0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[3]<=0:
												# {"feature": "Education", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[6]<=0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[5]>0:
										return 'True'
									else: return 'True'
								elif obj[4]>4:
									return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'True'
					elif obj[7]>18.52567473260329:
						# {"feature": "Bar", "instances": 97, "metric_value": 0.2374, "depth": 6}
						if obj[8]<=1.0:
							# {"feature": "Age", "instances": 69, "metric_value": 0.2925, "depth": 7}
							if obj[4]<=2:
								# {"feature": "Restaurant20to50", "instances": 44, "metric_value": 0.325, "depth": 8}
								if obj[10]<=1.0:
									# {"feature": "Time", "instances": 40, "metric_value": 0.2933, "depth": 9}
									if obj[1]>0:
										# {"feature": "Education", "instances": 30, "metric_value": 0.3753, "depth": 10}
										if obj[6]<=2:
											# {"feature": "Gender", "instances": 27, "metric_value": 0.4121, "depth": 11}
											if obj[3]>0:
												# {"feature": "Children", "instances": 22, "metric_value": 0.3955, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 12, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 10, "metric_value": 0.42, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Children", "instances": 5, "metric_value": 0.4667, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[6]>2:
											return 'True'
										else: return 'True'
									elif obj[1]<=0:
										return 'True'
									else: return 'True'
								elif obj[10]>1.0:
									# {"feature": "Children", "instances": 4, "metric_value": 0.25, "depth": 9}
									if obj[5]>0:
										return 'False'
									elif obj[5]<=0:
										# {"feature": "Time", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[1]<=3:
											# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Education", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[6]<=3:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[4]>2:
								# {"feature": "Time", "instances": 25, "metric_value": 0.1354, "depth": 8}
								if obj[1]>2:
									# {"feature": "Gender", "instances": 13, "metric_value": 0.241, "depth": 9}
									if obj[3]>0:
										# {"feature": "Education", "instances": 10, "metric_value": 0.1667, "depth": 10}
										if obj[6]<=0:
											# {"feature": "Children", "instances": 6, "metric_value": 0.2778, "depth": 11}
											if obj[5]<=1:
												# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.2778, "depth": 12}
												if obj[10]<=1.0:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.2778, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[6]>0:
											return 'True'
										else: return 'True'
									elif obj[3]<=0:
										# {"feature": "Children", "instances": 3, "metric_value": 0.0, "depth": 10}
										if obj[5]<=0:
											return 'True'
										elif obj[5]>0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[1]<=2:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[8]>1.0:
							# {"feature": "Age", "instances": 28, "metric_value": 0.0571, "depth": 7}
							if obj[4]<=2:
								return 'True'
							elif obj[4]>2:
								# {"feature": "Gender", "instances": 5, "metric_value": 0.2, "depth": 8}
								if obj[3]<=0:
									return 'True'
								elif obj[3]>0:
									# {"feature": "Education", "instances": 2, "metric_value": 0.0, "depth": 9}
									if obj[6]<=2:
										return 'False'
									elif obj[6]>2:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[12]>2:
				# {"feature": "Passanger", "instances": 417, "metric_value": 0.4857, "depth": 4}
				if obj[0]>0:
					# {"feature": "Age", "instances": 404, "metric_value": 0.486, "depth": 5}
					if obj[4]>0:
						# {"feature": "Time", "instances": 344, "metric_value": 0.4929, "depth": 6}
						if obj[1]>0:
							# {"feature": "Education", "instances": 295, "metric_value": 0.4958, "depth": 7}
							if obj[6]>0:
								# {"feature": "Occupation", "instances": 206, "metric_value": 0.4892, "depth": 8}
								if obj[7]<=18.03813645851065:
									# {"feature": "Restaurant20to50", "instances": 191, "metric_value": 0.4845, "depth": 9}
									if obj[10]<=3.0:
										# {"feature": "Bar", "instances": 187, "metric_value": 0.4905, "depth": 10}
										if obj[8]>-1.0:
											# {"feature": "Gender", "instances": 185, "metric_value": 0.4937, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Children", "instances": 97, "metric_value": 0.4931, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 67, "metric_value": 0.499, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 30, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[3]>0:
												# {"feature": "Children", "instances": 88, "metric_value": 0.4871, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 51, "metric_value": 0.4844, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 37, "metric_value": 0.4909, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[8]<=-1.0:
											return 'False'
										else: return 'False'
									elif obj[10]>3.0:
										return 'False'
									else: return 'False'
								elif obj[7]>18.03813645851065:
									# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.1905, "depth": 9}
									if obj[10]<=1.0:
										return 'True'
									elif obj[10]>1.0:
										# {"feature": "Gender", "instances": 7, "metric_value": 0.2857, "depth": 10}
										if obj[3]>0:
											# {"feature": "Children", "instances": 4, "metric_value": 0.3333, "depth": 11}
											if obj[5]>0:
												# {"feature": "Bar", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[8]<=2.0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[5]<=0:
												return 'True'
											else: return 'True'
										elif obj[3]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[6]<=0:
								# {"feature": "Occupation", "instances": 89, "metric_value": 0.4722, "depth": 8}
								if obj[7]<=9:
									# {"feature": "Restaurant20to50", "instances": 63, "metric_value": 0.452, "depth": 9}
									if obj[10]<=2.0:
										# {"feature": "Gender", "instances": 59, "metric_value": 0.459, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Bar", "instances": 30, "metric_value": 0.4196, "depth": 11}
											if obj[8]>0.0:
												# {"feature": "Children", "instances": 16, "metric_value": 0.4295, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 13, "metric_value": 0.426, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[8]<=0.0:
												# {"feature": "Children", "instances": 14, "metric_value": 0.4071, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 10, "metric_value": 0.42, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]>0:
											# {"feature": "Children", "instances": 29, "metric_value": 0.4516, "depth": 11}
											if obj[5]>0:
												# {"feature": "Bar", "instances": 15, "metric_value": 0.4103, "depth": 12}
												if obj[8]<=0.0:
													# {"feature": "Direction_same", "instances": 13, "metric_value": 0.4734, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[8]>0.0:
													return 'False'
												else: return 'False'
											elif obj[5]<=0:
												# {"feature": "Bar", "instances": 14, "metric_value": 0.449, "depth": 12}
												if obj[8]>0.0:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4898, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[8]<=0.0:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4082, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[10]>2.0:
										return 'True'
									else: return 'True'
								elif obj[7]>9:
									# {"feature": "Bar", "instances": 26, "metric_value": 0.4431, "depth": 9}
									if obj[8]<=3.0:
										# {"feature": "Children", "instances": 25, "metric_value": 0.4494, "depth": 10}
										if obj[5]>0:
											# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.414, "depth": 11}
											if obj[10]<=1.0:
												# {"feature": "Gender", "instances": 13, "metric_value": 0.3932, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 9, "metric_value": 0.3457, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[10]>1.0:
												# {"feature": "Gender", "instances": 4, "metric_value": 0.25, "depth": 12}
												if obj[3]>0:
													return 'True'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[5]<=0:
											# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.3, "depth": 11}
											if obj[10]<=1.0:
												# {"feature": "Gender", "instances": 5, "metric_value": 0.4667, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[10]>1.0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[8]>3.0:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'True'
						elif obj[1]<=0:
							# {"feature": "Education", "instances": 49, "metric_value": 0.4005, "depth": 7}
							if obj[6]<=2:
								# {"feature": "Restaurant20to50", "instances": 36, "metric_value": 0.4436, "depth": 8}
								if obj[10]<=1.0:
									# {"feature": "Bar", "instances": 26, "metric_value": 0.4185, "depth": 9}
									if obj[8]<=3.0:
										# {"feature": "Occupation", "instances": 25, "metric_value": 0.396, "depth": 10}
										if obj[7]>2:
											# {"feature": "Children", "instances": 20, "metric_value": 0.3529, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Gender", "instances": 17, "metric_value": 0.4078, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 12, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[5]>0:
												return 'False'
											else: return 'False'
										elif obj[7]<=2:
											# {"feature": "Children", "instances": 5, "metric_value": 0.2667, "depth": 11}
											if obj[5]>0:
												# {"feature": "Gender", "instances": 3, "metric_value": 0.3333, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													return 'False'
												else: return 'False'
											elif obj[5]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[8]>3.0:
										return 'True'
									else: return 'True'
								elif obj[10]>1.0:
									# {"feature": "Children", "instances": 10, "metric_value": 0.24, "depth": 9}
									if obj[5]<=0:
										# {"feature": "Occupation", "instances": 5, "metric_value": 0.2667, "depth": 10}
										if obj[7]<=7:
											# {"feature": "Gender", "instances": 3, "metric_value": 0.3333, "depth": 11}
											if obj[3]>0:
												# {"feature": "Bar", "instances": 2, "metric_value": 0.0, "depth": 12}
												if obj[8]>1.0:
													return 'False'
												elif obj[8]<=1.0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												return 'True'
											else: return 'True'
										elif obj[7]>7:
											return 'False'
										else: return 'False'
									elif obj[5]>0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[6]>2:
								# {"feature": "Occupation", "instances": 13, "metric_value": 0.0, "depth": 8}
								if obj[7]<=16:
									return 'False'
								elif obj[7]>16:
									return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'False'
					elif obj[4]<=0:
						# {"feature": "Education", "instances": 60, "metric_value": 0.35, "depth": 6}
						if obj[6]<=3:
							# {"feature": "Time", "instances": 56, "metric_value": 0.3542, "depth": 7}
							if obj[1]>0:
								# {"feature": "Occupation", "instances": 48, "metric_value": 0.3811, "depth": 8}
								if obj[7]<=10:
									# {"feature": "Bar", "instances": 39, "metric_value": 0.3419, "depth": 9}
									if obj[8]>0.0:
										# {"feature": "Restaurant20to50", "instances": 24, "metric_value": 0.2661, "depth": 10}
										if obj[10]<=1.0:
											# {"feature": "Gender", "instances": 17, "metric_value": 0.1882, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Children", "instances": 10, "metric_value": 0.3111, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 9, "metric_value": 0.3457, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[5]>0:
													return 'False'
												else: return 'False'
											elif obj[3]>0:
												return 'False'
											else: return 'False'
										elif obj[10]>1.0:
											# {"feature": "Children", "instances": 7, "metric_value": 0.3429, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Gender", "instances": 5, "metric_value": 0.48, "depth": 12}
												if obj[3]<=1:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[5]>0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[8]<=0.0:
										# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.4286, "depth": 10}
										if obj[10]<=2.0:
											# {"feature": "Gender", "instances": 14, "metric_value": 0.45, "depth": 11}
											if obj[3]>0:
												# {"feature": "Children", "instances": 10, "metric_value": 0.475, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.4688, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[5]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[3]<=0:
												# {"feature": "Children", "instances": 4, "metric_value": 0.25, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[5]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[10]>2.0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[7]>10:
									# {"feature": "Bar", "instances": 9, "metric_value": 0.1778, "depth": 9}
									if obj[8]<=1.0:
										# {"feature": "Children", "instances": 5, "metric_value": 0.2667, "depth": 10}
										if obj[5]>0:
											# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[3]<=1:
												# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=1.0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[5]<=0:
											return 'False'
										else: return 'False'
									elif obj[8]>1.0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[1]<=0:
								return 'False'
							else: return 'False'
						elif obj[6]>3:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[0]<=0:
					# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.2051, "depth": 5}
					if obj[10]<=1.0:
						return 'True'
					elif obj[10]>1.0:
						# {"feature": "Bar", "instances": 6, "metric_value": 0.0, "depth": 6}
						if obj[8]>1.0:
							return 'True'
						elif obj[8]<=1.0:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[9]<=0.0:
			# {"feature": "Passanger", "instances": 1457, "metric_value": 0.495, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Distance", "instances": 933, "metric_value": 0.4888, "depth": 4}
				if obj[12]<=1:
					# {"feature": "Time", "instances": 499, "metric_value": 0.4911, "depth": 5}
					if obj[1]>0:
						# {"feature": "Direction_same", "instances": 325, "metric_value": 0.478, "depth": 6}
						if obj[11]>0:
							# {"feature": "Education", "instances": 170, "metric_value": 0.4853, "depth": 7}
							if obj[6]>1:
								# {"feature": "Children", "instances": 103, "metric_value": 0.4719, "depth": 8}
								if obj[5]<=0:
									# {"feature": "Age", "instances": 69, "metric_value": 0.4723, "depth": 9}
									if obj[4]>0:
										# {"feature": "Occupation", "instances": 62, "metric_value": 0.4833, "depth": 10}
										if obj[7]<=20:
											# {"feature": "Gender", "instances": 60, "metric_value": 0.4889, "depth": 11}
											if obj[3]>0:
												# {"feature": "Restaurant20to50", "instances": 37, "metric_value": 0.4805, "depth": 12}
												if obj[10]<=2.0:
													# {"feature": "Bar", "instances": 36, "metric_value": 0.486, "depth": 13}
													if obj[8]<=1.0:
														return 'True'
													elif obj[8]>1.0:
														return 'False'
													else: return 'False'
												elif obj[10]>2.0:
													return 'False'
												else: return 'False'
											elif obj[3]<=0:
												# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.472, "depth": 12}
												if obj[10]>0.0:
													# {"feature": "Bar", "instances": 14, "metric_value": 0.4881, "depth": 13}
													if obj[8]<=2.0:
														return 'False'
													elif obj[8]>2.0:
														return 'True'
													else: return 'True'
												elif obj[10]<=0.0:
													# {"feature": "Bar", "instances": 9, "metric_value": 0.4167, "depth": 13}
													if obj[8]>0.0:
														return 'False'
													elif obj[8]<=0.0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[7]>20:
											return 'False'
										else: return 'False'
									elif obj[4]<=0:
										# {"feature": "Occupation", "instances": 7, "metric_value": 0.1905, "depth": 10}
										if obj[7]<=8:
											return 'True'
										elif obj[7]>8:
											# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Bar", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[8]<=2.0:
													# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[10]<=1.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[5]>0:
									# {"feature": "Restaurant20to50", "instances": 34, "metric_value": 0.3805, "depth": 9}
									if obj[10]>0.0:
										# {"feature": "Occupation", "instances": 21, "metric_value": 0.2424, "depth": 10}
										if obj[7]>9:
											# {"feature": "Bar", "instances": 11, "metric_value": 0.3818, "depth": 11}
											if obj[8]<=1.0:
												# {"feature": "Gender", "instances": 10, "metric_value": 0.4, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Age", "instances": 8, "metric_value": 0.3333, "depth": 13}
													if obj[4]>2:
														return 'False'
													elif obj[4]<=2:
														return 'False'
													else: return 'False'
												elif obj[3]>0:
													# {"feature": "Age", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[4]<=2:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[8]>1.0:
												return 'True'
											else: return 'True'
										elif obj[7]<=9:
											return 'False'
										else: return 'False'
									elif obj[10]<=0.0:
										# {"feature": "Age", "instances": 13, "metric_value": 0.4487, "depth": 10}
										if obj[4]<=3:
											# {"feature": "Occupation", "instances": 12, "metric_value": 0.4242, "depth": 11}
											if obj[7]>2:
												# {"feature": "Gender", "instances": 11, "metric_value": 0.4545, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Bar", "instances": 9, "metric_value": 0.4444, "depth": 13}
													if obj[8]<=0.0:
														return 'False'
													else: return 'False'
												elif obj[3]>0:
													# {"feature": "Bar", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[8]<=0.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[7]<=2:
												return 'True'
											else: return 'True'
										elif obj[4]>3:
											return 'True'
										else: return 'True'
									else: return 'False'
								else: return 'False'
							elif obj[6]<=1:
								# {"feature": "Bar", "instances": 67, "metric_value": 0.4411, "depth": 8}
								if obj[8]<=1.0:
									# {"feature": "Restaurant20to50", "instances": 55, "metric_value": 0.3984, "depth": 9}
									if obj[10]<=1.0:
										# {"feature": "Occupation", "instances": 46, "metric_value": 0.439, "depth": 10}
										if obj[7]<=12:
											# {"feature": "Gender", "instances": 41, "metric_value": 0.4713, "depth": 11}
											if obj[3]>0:
												# {"feature": "Age", "instances": 23, "metric_value": 0.4417, "depth": 12}
												if obj[4]>2:
													# {"feature": "Children", "instances": 14, "metric_value": 0.4048, "depth": 13}
													if obj[5]>0:
														return 'True'
													elif obj[5]<=0:
														return 'True'
													else: return 'True'
												elif obj[4]<=2:
													# {"feature": "Children", "instances": 9, "metric_value": 0.4815, "depth": 13}
													if obj[5]>0:
														return 'True'
													elif obj[5]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Age", "instances": 18, "metric_value": 0.4618, "depth": 12}
												if obj[4]>2:
													# {"feature": "Children", "instances": 11, "metric_value": 0.4959, "depth": 13}
													if obj[5]<=0:
														return 'True'
													else: return 'True'
												elif obj[4]<=2:
													# {"feature": "Children", "instances": 7, "metric_value": 0.4048, "depth": 13}
													if obj[5]>0:
														return 'False'
													elif obj[5]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[7]>12:
											return 'True'
										else: return 'True'
									elif obj[10]>1.0:
										return 'True'
									else: return 'True'
								elif obj[8]>1.0:
									# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.3429, "depth": 9}
									if obj[10]<=1.0:
										# {"feature": "Age", "instances": 7, "metric_value": 0.1429, "depth": 10}
										if obj[4]>0:
											return 'False'
										elif obj[4]<=0:
											# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Occupation", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[7]<=10:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[10]>1.0:
										# {"feature": "Gender", "instances": 5, "metric_value": 0.4, "depth": 10}
										if obj[3]>0:
											# {"feature": "Age", "instances": 4, "metric_value": 0.5, "depth": 11}
											if obj[4]<=1:
												# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[5]<=1:
													# {"feature": "Occupation", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[7]<=10:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[4]>1:
												# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Occupation", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[7]<=18:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'True'
						elif obj[11]<=0:
							# {"feature": "Bar", "instances": 155, "metric_value": 0.4437, "depth": 7}
							if obj[8]<=0.0:
								# {"feature": "Occupation", "instances": 82, "metric_value": 0.3864, "depth": 8}
								if obj[7]<=6:
									# {"feature": "Age", "instances": 51, "metric_value": 0.44, "depth": 9}
									if obj[4]<=6:
										# {"feature": "Children", "instances": 50, "metric_value": 0.4375, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Gender", "instances": 33, "metric_value": 0.4187, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Education", "instances": 22, "metric_value": 0.3732, "depth": 12}
												if obj[6]<=3:
													# {"feature": "Restaurant20to50", "instances": 19, "metric_value": 0.3947, "depth": 13}
													if obj[10]<=1.0:
														return 'True'
													elif obj[10]>1.0:
														return 'True'
													else: return 'True'
												elif obj[6]>3:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Education", "instances": 11, "metric_value": 0.2424, "depth": 12}
												if obj[6]>0:
													# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.2667, "depth": 13}
													if obj[10]>0.0:
														return 'True'
													elif obj[10]<=0.0:
														return 'False'
													else: return 'False'
												elif obj[6]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[5]>0:
											# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.2868, "depth": 11}
											if obj[10]>-1.0:
												# {"feature": "Education", "instances": 16, "metric_value": 0.2727, "depth": 12}
												if obj[6]<=0:
													# {"feature": "Gender", "instances": 11, "metric_value": 0.3818, "depth": 13}
													if obj[3]>0:
														return 'True'
													elif obj[3]<=0:
														return 'True'
													else: return 'True'
												elif obj[6]>0:
													return 'True'
												else: return 'True'
											elif obj[10]<=-1.0:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[4]>6:
										return 'False'
									else: return 'False'
								elif obj[7]>6:
									# {"feature": "Gender", "instances": 31, "metric_value": 0.233, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Age", "instances": 18, "metric_value": 0.3519, "depth": 10}
										if obj[4]>2:
											# {"feature": "Education", "instances": 12, "metric_value": 0.2381, "depth": 11}
											if obj[6]<=0:
												# {"feature": "Children", "instances": 7, "metric_value": 0.381, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.4, "depth": 13}
													if obj[10]>-1.0:
														return 'True'
													elif obj[10]<=-1.0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													return 'True'
												else: return 'True'
											elif obj[6]>0:
												return 'True'
											else: return 'True'
										elif obj[4]<=2:
											# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.25, "depth": 11}
											if obj[10]>0.0:
												# {"feature": "Children", "instances": 4, "metric_value": 0.3333, "depth": 12}
												if obj[5]>0:
													# {"feature": "Education", "instances": 3, "metric_value": 0.3333, "depth": 13}
													if obj[6]<=0:
														return 'False'
													elif obj[6]>0:
														return 'False'
													else: return 'False'
												elif obj[5]<=0:
													return 'False'
												else: return 'False'
											elif obj[10]<=0.0:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[3]>0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[8]>0.0:
								# {"feature": "Restaurant20to50", "instances": 73, "metric_value": 0.447, "depth": 8}
								if obj[10]>0.0:
									# {"feature": "Occupation", "instances": 61, "metric_value": 0.4307, "depth": 9}
									if obj[7]<=6:
										# {"feature": "Age", "instances": 34, "metric_value": 0.4836, "depth": 10}
										if obj[4]<=4:
											# {"feature": "Gender", "instances": 26, "metric_value": 0.4615, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Education", "instances": 18, "metric_value": 0.475, "depth": 12}
												if obj[6]>0:
													# {"feature": "Children", "instances": 10, "metric_value": 0.419, "depth": 13}
													if obj[5]<=0:
														return 'False'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												elif obj[6]<=0:
													# {"feature": "Children", "instances": 8, "metric_value": 0.4688, "depth": 13}
													if obj[5]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Education", "instances": 8, "metric_value": 0.3, "depth": 12}
												if obj[6]>2:
													# {"feature": "Children", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[5]<=0:
														return 'True'
													else: return 'True'
												elif obj[6]<=2:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[4]>4:
											# {"feature": "Children", "instances": 8, "metric_value": 0.4375, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Gender", "instances": 4, "metric_value": 0.3333, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Education", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[6]<=2:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													return 'False'
												else: return 'False'
											elif obj[5]>0:
												# {"feature": "Gender", "instances": 4, "metric_value": 0.25, "depth": 12}
												if obj[3]>0:
													# {"feature": "Education", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[6]<=2:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[7]>6:
										# {"feature": "Age", "instances": 27, "metric_value": 0.3188, "depth": 10}
										if obj[4]<=6:
											# {"feature": "Children", "instances": 23, "metric_value": 0.266, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Education", "instances": 17, "metric_value": 0.3252, "depth": 12}
												if obj[6]<=1:
													# {"feature": "Gender", "instances": 9, "metric_value": 0.1905, "depth": 13}
													if obj[3]<=0:
														return 'True'
													elif obj[3]>0:
														return 'True'
													else: return 'True'
												elif obj[6]>1:
													# {"feature": "Gender", "instances": 8, "metric_value": 0.4667, "depth": 13}
													if obj[3]<=0:
														return 'True'
													elif obj[3]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[5]>0:
												return 'True'
											else: return 'True'
										elif obj[4]>6:
											# {"feature": "Gender", "instances": 4, "metric_value": 0.5, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Children", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[5]<=1:
													# {"feature": "Education", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[6]<=2:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[10]<=0.0:
									# {"feature": "Occupation", "instances": 12, "metric_value": 0.25, "depth": 9}
									if obj[7]>8:
										return 'False'
									elif obj[7]<=8:
										# {"feature": "Age", "instances": 6, "metric_value": 0.4, "depth": 10}
										if obj[4]<=4:
											# {"feature": "Education", "instances": 5, "metric_value": 0.4, "depth": 11}
											if obj[6]<=2:
												# {"feature": "Gender", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[3]>0:
													# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[5]<=1:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[5]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[6]>2:
												return 'True'
											else: return 'True'
										elif obj[4]>4:
											return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					elif obj[1]<=0:
						# {"feature": "Occupation", "instances": 174, "metric_value": 0.4654, "depth": 6}
						if obj[7]<=6:
							# {"feature": "Education", "instances": 94, "metric_value": 0.4397, "depth": 7}
							if obj[6]<=4:
								# {"feature": "Bar", "instances": 93, "metric_value": 0.4348, "depth": 8}
								if obj[8]>-1.0:
									# {"feature": "Age", "instances": 92, "metric_value": 0.4345, "depth": 9}
									if obj[4]>1:
										# {"feature": "Direction_same", "instances": 50, "metric_value": 0.4007, "depth": 10}
										if obj[11]<=0:
											# {"feature": "Children", "instances": 29, "metric_value": 0.4079, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.441, "depth": 12}
												if obj[10]>0.0:
													# {"feature": "Gender", "instances": 13, "metric_value": 0.3419, "depth": 13}
													if obj[3]<=0:
														return 'False'
													elif obj[3]>0:
														return 'False'
													else: return 'False'
												elif obj[10]<=0.0:
													# {"feature": "Gender", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[3]<=1:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[5]>0:
												# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.1636, "depth": 12}
												if obj[10]<=1.0:
													# {"feature": "Gender", "instances": 10, "metric_value": 0.1714, "depth": 13}
													if obj[3]>0:
														return 'False'
													elif obj[3]<=0:
														return 'False'
													else: return 'False'
												elif obj[10]>1.0:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[11]>0:
											# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.3509, "depth": 11}
											if obj[10]<=1.0:
												# {"feature": "Gender", "instances": 19, "metric_value": 0.3746, "depth": 12}
												if obj[3]>0:
													# {"feature": "Children", "instances": 17, "metric_value": 0.3597, "depth": 13}
													if obj[5]<=0:
														return 'False'
													elif obj[5]>0:
														return 'False'
													else: return 'False'
												elif obj[3]<=0:
													# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[5]<=1:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[10]>1.0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[4]<=1:
										# {"feature": "Children", "instances": 42, "metric_value": 0.4603, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Restaurant20to50", "instances": 30, "metric_value": 0.4368, "depth": 11}
											if obj[10]>0.0:
												# {"feature": "Direction_same", "instances": 29, "metric_value": 0.4496, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Gender", "instances": 16, "metric_value": 0.4682, "depth": 13}
													if obj[3]<=0:
														return 'False'
													elif obj[3]>0:
														return 'False'
													else: return 'False'
												elif obj[11]>0:
													# {"feature": "Gender", "instances": 13, "metric_value": 0.4256, "depth": 13}
													if obj[3]<=0:
														return 'False'
													elif obj[3]>0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[10]<=0.0:
												return 'False'
											else: return 'False'
										elif obj[5]>0:
											# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.4, "depth": 11}
											if obj[10]<=1.0:
												# {"feature": "Gender", "instances": 10, "metric_value": 0.4, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.3, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.2, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												else: return 'True'
											elif obj[10]>1.0:
												return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'False'
								elif obj[8]<=-1.0:
									return 'True'
								else: return 'True'
							elif obj[6]>4:
								return 'True'
							else: return 'True'
						elif obj[7]>6:
							# {"feature": "Direction_same", "instances": 80, "metric_value": 0.4492, "depth": 7}
							if obj[11]>0:
								# {"feature": "Age", "instances": 42, "metric_value": 0.3956, "depth": 8}
								if obj[4]<=6:
									# {"feature": "Restaurant20to50", "instances": 39, "metric_value": 0.4158, "depth": 9}
									if obj[10]>-1.0:
										# {"feature": "Bar", "instances": 37, "metric_value": 0.4324, "depth": 10}
										if obj[8]<=2.0:
											# {"feature": "Children", "instances": 36, "metric_value": 0.4401, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Gender", "instances": 29, "metric_value": 0.4246, "depth": 12}
												if obj[3]>0:
													# {"feature": "Education", "instances": 18, "metric_value": 0.3819, "depth": 13}
													if obj[6]<=3:
														return 'True'
													elif obj[6]>3:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													# {"feature": "Education", "instances": 11, "metric_value": 0.4545, "depth": 13}
													if obj[6]<=3:
														return 'True'
													elif obj[6]>3:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[5]>0:
												# {"feature": "Education", "instances": 7, "metric_value": 0.4762, "depth": 12}
												if obj[6]>0:
													# {"feature": "Gender", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[3]<=0:
														return 'True'
													else: return 'True'
												elif obj[6]<=0:
													# {"feature": "Gender", "instances": 3, "metric_value": 0.3333, "depth": 13}
													if obj[3]>0:
														return 'False'
													elif obj[3]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[8]>2.0:
											return 'True'
										else: return 'True'
									elif obj[10]<=-1.0:
										return 'True'
									else: return 'True'
								elif obj[4]>6:
									return 'True'
								else: return 'True'
							elif obj[11]<=0:
								# {"feature": "Age", "instances": 38, "metric_value": 0.4598, "depth": 8}
								if obj[4]<=2:
									# {"feature": "Education", "instances": 19, "metric_value": 0.3801, "depth": 9}
									if obj[6]<=3:
										# {"feature": "Bar", "instances": 18, "metric_value": 0.3704, "depth": 10}
										if obj[8]<=2.0:
											# {"feature": "Children", "instances": 15, "metric_value": 0.4074, "depth": 11}
											if obj[5]>0:
												# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.2963, "depth": 12}
												if obj[10]>0.0:
													# {"feature": "Gender", "instances": 6, "metric_value": 0.3333, "depth": 13}
													if obj[3]<=0:
														return 'False'
													elif obj[3]>0:
														return 'False'
													else: return 'False'
												elif obj[10]<=0.0:
													return 'False'
												else: return 'False'
											elif obj[5]<=0:
												# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.4, "depth": 12}
												if obj[10]<=1.0:
													# {"feature": "Gender", "instances": 5, "metric_value": 0.4667, "depth": 13}
													if obj[3]>0:
														return 'False'
													elif obj[3]<=0:
														return 'True'
													else: return 'True'
												elif obj[10]>1.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[8]>2.0:
											return 'False'
										else: return 'False'
									elif obj[6]>3:
										return 'True'
									else: return 'True'
								elif obj[4]>2:
									# {"feature": "Bar", "instances": 19, "metric_value": 0.3789, "depth": 9}
									if obj[8]<=0.0:
										# {"feature": "Education", "instances": 10, "metric_value": 0.2857, "depth": 10}
										if obj[6]>0:
											# {"feature": "Children", "instances": 7, "metric_value": 0.3714, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.2, "depth": 12}
												if obj[10]<=1.0:
													return 'True'
												elif obj[10]>1.0:
													# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[3]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[5]>0:
												# {"feature": "Gender", "instances": 2, "metric_value": 0.0, "depth": 12}
												if obj[3]>0:
													return 'False'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[6]<=0:
											return 'True'
										else: return 'True'
									elif obj[8]>0.0:
										# {"feature": "Children", "instances": 9, "metric_value": 0.381, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Gender", "instances": 7, "metric_value": 0.4286, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.4, "depth": 12}
												if obj[10]>0.0:
													# {"feature": "Education", "instances": 5, "metric_value": 0.4, "depth": 13}
													if obj[6]<=1:
														return 'True'
													elif obj[6]>1:
														return 'True'
													else: return 'True'
												elif obj[10]<=0.0:
													return 'False'
												else: return 'False'
											elif obj[3]>0:
												return 'False'
											else: return 'False'
										elif obj[5]>0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'False'
						else: return 'True'
					else: return 'False'
				elif obj[12]>1:
					# {"feature": "Education", "instances": 434, "metric_value": 0.4739, "depth": 5}
					if obj[6]>1:
						# {"feature": "Bar", "instances": 258, "metric_value": 0.4526, "depth": 6}
						if obj[8]<=1.0:
							# {"feature": "Occupation", "instances": 202, "metric_value": 0.4655, "depth": 7}
							if obj[7]<=9:
								# {"feature": "Time", "instances": 134, "metric_value": 0.4758, "depth": 8}
								if obj[1]>0:
									# {"feature": "Direction_same", "instances": 107, "metric_value": 0.4829, "depth": 9}
									if obj[11]<=0:
										# {"feature": "Restaurant20to50", "instances": 89, "metric_value": 0.4818, "depth": 10}
										if obj[10]>0.0:
											# {"feature": "Age", "instances": 58, "metric_value": 0.4655, "depth": 11}
											if obj[4]>0:
												# {"feature": "Gender", "instances": 50, "metric_value": 0.4787, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Children", "instances": 34, "metric_value": 0.4695, "depth": 13}
													if obj[5]<=0:
														return 'False'
													elif obj[5]>0:
														return 'False'
													else: return 'False'
												elif obj[3]>0:
													# {"feature": "Children", "instances": 16, "metric_value": 0.4844, "depth": 13}
													if obj[5]>0:
														return 'False'
													elif obj[5]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[4]<=0:
												# {"feature": "Children", "instances": 8, "metric_value": 0.2143, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Gender", "instances": 7, "metric_value": 0.2449, "depth": 13}
													if obj[3]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[10]<=0.0:
											# {"feature": "Age", "instances": 31, "metric_value": 0.4305, "depth": 11}
											if obj[4]>2:
												# {"feature": "Children", "instances": 24, "metric_value": 0.4028, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Gender", "instances": 18, "metric_value": 0.4333, "depth": 13}
													if obj[3]>0:
														return 'True'
													elif obj[3]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Gender", "instances": 6, "metric_value": 0.25, "depth": 13}
													if obj[3]<=0:
														return 'True'
													elif obj[3]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[4]<=2:
												# {"feature": "Children", "instances": 7, "metric_value": 0.4762, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Gender", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[3]<=1:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Gender", "instances": 3, "metric_value": 0.3333, "depth": 13}
													if obj[3]<=0:
														return 'True'
													elif obj[3]>0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[11]>0:
										# {"feature": "Age", "instances": 18, "metric_value": 0.3399, "depth": 10}
										if obj[4]<=6:
											# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.3076, "depth": 11}
											if obj[10]<=1.0:
												# {"feature": "Children", "instances": 10, "metric_value": 0.1333, "depth": 12}
												if obj[5]<=0:
													return 'False'
												elif obj[5]>0:
													# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[3]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[10]>1.0:
												# {"feature": "Gender", "instances": 7, "metric_value": 0.381, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Children", "instances": 6, "metric_value": 0.4, "depth": 13}
													if obj[5]<=0:
														return 'False'
													elif obj[5]>0:
														return 'False'
													else: return 'False'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[4]>6:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[1]<=0:
									# {"feature": "Age", "instances": 27, "metric_value": 0.3498, "depth": 9}
									if obj[4]>1:
										# {"feature": "Gender", "instances": 18, "metric_value": 0.25, "depth": 10}
										if obj[3]>0:
											# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.2727, "depth": 11}
											if obj[10]<=1.0:
												# {"feature": "Children", "instances": 11, "metric_value": 0.2727, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.3667, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												elif obj[5]>0:
													return 'False'
												else: return 'False'
											elif obj[10]>1.0:
												return 'True'
											else: return 'True'
										elif obj[3]<=0:
											return 'False'
										else: return 'False'
									elif obj[4]<=1:
										# {"feature": "Direction_same", "instances": 9, "metric_value": 0.3175, "depth": 10}
										if obj[11]<=0:
											# {"feature": "Children", "instances": 7, "metric_value": 0.381, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.4167, "depth": 12}
												if obj[10]>1.0:
													# {"feature": "Gender", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[3]<=0:
														return 'False'
													else: return 'False'
												elif obj[10]<=1.0:
													# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[3]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[5]>0:
												return 'False'
											else: return 'False'
										elif obj[11]>0:
											return 'True'
										else: return 'True'
									else: return 'False'
								else: return 'False'
							elif obj[7]>9:
								# {"feature": "Children", "instances": 68, "metric_value": 0.3965, "depth": 8}
								if obj[5]<=0:
									# {"feature": "Time", "instances": 40, "metric_value": 0.4487, "depth": 9}
									if obj[1]<=2:
										# {"feature": "Age", "instances": 27, "metric_value": 0.4656, "depth": 10}
										if obj[4]>1:
											# {"feature": "Gender", "instances": 21, "metric_value": 0.4603, "depth": 11}
											if obj[3]>0:
												# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.4074, "depth": 12}
												if obj[10]<=0.0:
													# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4921, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[10]>0.0:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.2222, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[3]<=0:
												# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.25, "depth": 12}
												if obj[10]>0.0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.25, "depth": 13}
													if obj[11]>0:
														return 'True'
													elif obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[10]<=0.0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[4]<=1:
											# {"feature": "Gender", "instances": 6, "metric_value": 0.4, "depth": 11}
											if obj[3]>0:
												# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.3, "depth": 12}
												if obj[10]>0.0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.3333, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[10]<=0.0:
													return 'False'
												else: return 'False'
											elif obj[3]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[1]>2:
										# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.2564, "depth": 10}
										if obj[10]<=1.0:
											# {"feature": "Gender", "instances": 12, "metric_value": 0.2222, "depth": 11}
											if obj[3]>0:
												return 'False'
											elif obj[3]<=0:
												# {"feature": "Age", "instances": 6, "metric_value": 0.3333, "depth": 12}
												if obj[4]>2:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[4]<=2:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[10]>1.0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[5]>0:
									# {"feature": "Restaurant20to50", "instances": 28, "metric_value": 0.249, "depth": 9}
									if obj[10]>0.0:
										# {"feature": "Age", "instances": 17, "metric_value": 0.1029, "depth": 10}
										if obj[4]<=2:
											return 'False'
										elif obj[4]>2:
											# {"feature": "Time", "instances": 8, "metric_value": 0.2, "depth": 11}
											if obj[1]<=1:
												# {"feature": "Gender", "instances": 5, "metric_value": 0.3, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]>0:
													return 'False'
												else: return 'False'
											elif obj[1]>1:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[10]<=0.0:
										# {"feature": "Time", "instances": 11, "metric_value": 0.2828, "depth": 10}
										if obj[1]<=3:
											# {"feature": "Direction_same", "instances": 9, "metric_value": 0.3016, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Gender", "instances": 7, "metric_value": 0.2143, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Age", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[4]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]>0:
													return 'False'
												else: return 'False'
											elif obj[11]>0:
												# {"feature": "Gender", "instances": 2, "metric_value": 0.0, "depth": 12}
												if obj[3]<=0:
													return 'False'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[1]>3:
											return 'True'
										else: return 'True'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[8]>1.0:
							# {"feature": "Occupation", "instances": 56, "metric_value": 0.3569, "depth": 7}
							if obj[7]>3:
								# {"feature": "Restaurant20to50", "instances": 43, "metric_value": 0.4027, "depth": 8}
								if obj[10]<=1.0:
									# {"feature": "Age", "instances": 30, "metric_value": 0.459, "depth": 9}
									if obj[4]<=4:
										# {"feature": "Time", "instances": 26, "metric_value": 0.4424, "depth": 10}
										if obj[1]<=1:
											# {"feature": "Children", "instances": 17, "metric_value": 0.4044, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Gender", "instances": 16, "metric_value": 0.4295, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 13, "metric_value": 0.4126, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.3333, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[5]>0:
												return 'False'
											else: return 'False'
										elif obj[1]>1:
											# {"feature": "Gender", "instances": 9, "metric_value": 0.4444, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Children", "instances": 8, "metric_value": 0.5, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[3]>0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[4]>4:
										# {"feature": "Direction_same", "instances": 4, "metric_value": 0.3333, "depth": 10}
										if obj[11]<=0:
											# {"feature": "Time", "instances": 3, "metric_value": 0.3333, "depth": 11}
											if obj[1]>0:
												# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[5]<=1:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[1]<=0:
												return 'False'
											else: return 'False'
										elif obj[11]>0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[10]>1.0:
									# {"feature": "Direction_same", "instances": 13, "metric_value": 0.141, "depth": 9}
									if obj[11]<=0:
										# {"feature": "Time", "instances": 12, "metric_value": 0.1111, "depth": 10}
										if obj[1]<=1:
											return 'False'
										elif obj[1]>1:
											# {"feature": "Age", "instances": 3, "metric_value": 0.3333, "depth": 11}
											if obj[4]<=1:
												# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[5]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[4]>1:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[11]>0:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[7]<=3:
								# {"feature": "Time", "instances": 13, "metric_value": 0.1282, "depth": 8}
								if obj[1]<=1:
									return 'False'
								elif obj[1]>1:
									# {"feature": "Gender", "instances": 6, "metric_value": 0.2222, "depth": 9}
									if obj[3]>0:
										# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.3333, "depth": 10}
										if obj[10]>1.0:
											# {"feature": "Age", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[4]<=1:
												# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[10]<=1.0:
											return 'False'
										else: return 'False'
									elif obj[3]<=0:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[6]<=1:
						# {"feature": "Occupation", "instances": 176, "metric_value": 0.483, "depth": 6}
						if obj[7]>3:
							# {"feature": "Age", "instances": 115, "metric_value": 0.483, "depth": 7}
							if obj[4]>3:
								# {"feature": "Restaurant20to50", "instances": 58, "metric_value": 0.457, "depth": 8}
								if obj[10]<=1.0:
									# {"feature": "Time", "instances": 41, "metric_value": 0.4833, "depth": 9}
									if obj[1]<=1:
										# {"feature": "Direction_same", "instances": 29, "metric_value": 0.4849, "depth": 10}
										if obj[11]<=0:
											# {"feature": "Bar", "instances": 19, "metric_value": 0.4526, "depth": 11}
											if obj[8]<=0.0:
												# {"feature": "Gender", "instances": 14, "metric_value": 0.4889, "depth": 12}
												if obj[3]>0:
													# {"feature": "Children", "instances": 9, "metric_value": 0.4815, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'False'
													else: return 'False'
												elif obj[3]<=0:
													# {"feature": "Children", "instances": 5, "metric_value": 0.4667, "depth": 13}
													if obj[5]>0:
														return 'True'
													elif obj[5]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[8]>0.0:
												# {"feature": "Gender", "instances": 5, "metric_value": 0.2, "depth": 12}
												if obj[3]<=0:
													return 'False'
												elif obj[3]>0:
													# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[5]<=1:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[11]>0:
											# {"feature": "Bar", "instances": 10, "metric_value": 0.4, "depth": 11}
											if obj[8]<=0.0:
												# {"feature": "Gender", "instances": 8, "metric_value": 0.4286, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Children", "instances": 7, "metric_value": 0.3429, "depth": 13}
													if obj[5]<=0:
														return 'False'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													return 'False'
												else: return 'False'
											elif obj[8]>0.0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[1]>1:
										# {"feature": "Gender", "instances": 12, "metric_value": 0.3636, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Bar", "instances": 11, "metric_value": 0.3636, "depth": 11}
											if obj[8]<=0.0:
												# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4167, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Children", "instances": 8, "metric_value": 0.4688, "depth": 13}
													if obj[5]<=0:
														return 'True'
													else: return 'True'
												elif obj[11]>0:
													return 'True'
												else: return 'True'
											elif obj[8]>0.0:
												return 'True'
											else: return 'True'
										elif obj[3]>0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[10]>1.0:
									# {"feature": "Children", "instances": 17, "metric_value": 0.3258, "depth": 9}
									if obj[5]<=0:
										# {"feature": "Direction_same", "instances": 13, "metric_value": 0.4103, "depth": 10}
										if obj[11]<=0:
											# {"feature": "Time", "instances": 12, "metric_value": 0.3636, "depth": 11}
											if obj[1]>0:
												# {"feature": "Gender", "instances": 11, "metric_value": 0.3409, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Bar", "instances": 8, "metric_value": 0.4583, "depth": 13}
													if obj[8]<=1.0:
														return 'True'
													elif obj[8]>1.0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											elif obj[1]<=0:
												return 'False'
											else: return 'False'
										elif obj[11]>0:
											return 'True'
										else: return 'True'
									elif obj[5]>0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[4]<=3:
								# {"feature": "Time", "instances": 57, "metric_value": 0.4808, "depth": 8}
								if obj[1]>0:
									# {"feature": "Restaurant20to50", "instances": 48, "metric_value": 0.474, "depth": 9}
									if obj[10]<=1.0:
										# {"feature": "Bar", "instances": 40, "metric_value": 0.4654, "depth": 10}
										if obj[8]<=2.0:
											# {"feature": "Direction_same", "instances": 33, "metric_value": 0.4641, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Children", "instances": 28, "metric_value": 0.4848, "depth": 12}
												if obj[5]>0:
													# {"feature": "Gender", "instances": 22, "metric_value": 0.4924, "depth": 13}
													if obj[3]<=0:
														return 'False'
													elif obj[3]>0:
														return 'False'
													else: return 'False'
												elif obj[5]<=0:
													# {"feature": "Gender", "instances": 6, "metric_value": 0.3333, "depth": 13}
													if obj[3]<=0:
														return 'True'
													elif obj[3]>0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[11]>0:
												# {"feature": "Children", "instances": 5, "metric_value": 0.0, "depth": 12}
												if obj[5]>0:
													return 'False'
												elif obj[5]<=0:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[8]>2.0:
											# {"feature": "Direction_same", "instances": 7, "metric_value": 0.3714, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Gender", "instances": 5, "metric_value": 0.32, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Children", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[5]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[11]>0:
												# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[5]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[10]>1.0:
										# {"feature": "Bar", "instances": 8, "metric_value": 0.4667, "depth": 10}
										if obj[8]>1.0:
											# {"feature": "Direction_same", "instances": 5, "metric_value": 0.3, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Gender", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[3]<=1:
													# {"feature": "Children", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[5]<=1:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[11]>0:
												return 'False'
											else: return 'False'
										elif obj[8]<=1.0:
											# {"feature": "Direction_same", "instances": 3, "metric_value": 0.0, "depth": 11}
											if obj[11]<=0:
												return 'False'
											elif obj[11]>0:
												return 'True'
											else: return 'True'
										else: return 'False'
									else: return 'False'
								elif obj[1]<=0:
									# {"feature": "Gender", "instances": 9, "metric_value": 0.381, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.3429, "depth": 10}
										if obj[10]<=0.0:
											# {"feature": "Direction_same", "instances": 5, "metric_value": 0.2667, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Children", "instances": 3, "metric_value": 0.3333, "depth": 12}
												if obj[5]>0:
													# {"feature": "Bar", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[8]<=0.0:
														return 'False'
													else: return 'False'
												elif obj[5]<=0:
													return 'False'
												else: return 'False'
											elif obj[11]>0:
												return 'True'
											else: return 'True'
										elif obj[10]>0.0:
											return 'False'
										else: return 'False'
									elif obj[3]>0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[7]<=3:
							# {"feature": "Restaurant20to50", "instances": 61, "metric_value": 0.4312, "depth": 7}
							if obj[10]>0.0:
								# {"feature": "Direction_same", "instances": 41, "metric_value": 0.4253, "depth": 8}
								if obj[11]<=0:
									# {"feature": "Time", "instances": 35, "metric_value": 0.4114, "depth": 9}
									if obj[1]>0:
										# {"feature": "Bar", "instances": 30, "metric_value": 0.4528, "depth": 10}
										if obj[8]<=1.0:
											# {"feature": "Age", "instances": 24, "metric_value": 0.4444, "depth": 11}
											if obj[4]>1:
												# {"feature": "Gender", "instances": 15, "metric_value": 0.4267, "depth": 12}
												if obj[3]>0:
													# {"feature": "Children", "instances": 10, "metric_value": 0.4762, "depth": 13}
													if obj[5]>0:
														return 'False'
													elif obj[5]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]<=0:
													# {"feature": "Children", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[5]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[4]<=1:
												# {"feature": "Gender", "instances": 9, "metric_value": 0.3333, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Children", "instances": 6, "metric_value": 0.25, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Children", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[5]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[8]>1.0:
											# {"feature": "Age", "instances": 6, "metric_value": 0.2222, "depth": 11}
											if obj[4]>0:
												# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Children", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[5]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[4]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[1]<=0:
										return 'False'
									else: return 'False'
								elif obj[11]>0:
									# {"feature": "Age", "instances": 6, "metric_value": 0.0, "depth": 9}
									if obj[4]>0:
										return 'True'
									elif obj[4]<=0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[10]<=0.0:
								# {"feature": "Children", "instances": 20, "metric_value": 0.275, "depth": 8}
								if obj[5]>0:
									# {"feature": "Age", "instances": 16, "metric_value": 0.1944, "depth": 9}
									if obj[4]>2:
										# {"feature": "Time", "instances": 9, "metric_value": 0.2963, "depth": 10}
										if obj[1]>0:
											# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Gender", "instances": 5, "metric_value": 0.3, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Bar", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[8]<=0.0:
														return 'False'
													else: return 'False'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											elif obj[11]>0:
												return 'False'
											else: return 'False'
										elif obj[1]<=0:
											return 'False'
										else: return 'False'
									elif obj[4]<=2:
										return 'False'
									else: return 'False'
								elif obj[5]<=0:
									# {"feature": "Time", "instances": 4, "metric_value": 0.3333, "depth": 9}
									if obj[1]>0:
										# {"feature": "Gender", "instances": 3, "metric_value": 0.3333, "depth": 10}
										if obj[3]>0:
											# {"feature": "Age", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[4]<=2:
												# {"feature": "Bar", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[8]<=0.0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]<=0:
											return 'False'
										else: return 'False'
									elif obj[1]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[0]>1:
				# {"feature": "Distance", "instances": 524, "metric_value": 0.4635, "depth": 4}
				if obj[12]>1:
					# {"feature": "Occupation", "instances": 349, "metric_value": 0.4481, "depth": 5}
					if obj[7]>1.5048799563075503:
						# {"feature": "Time", "instances": 290, "metric_value": 0.4613, "depth": 6}
						if obj[1]<=2:
							# {"feature": "Education", "instances": 169, "metric_value": 0.4664, "depth": 7}
							if obj[6]<=2:
								# {"feature": "Restaurant20to50", "instances": 140, "metric_value": 0.4914, "depth": 8}
								if obj[10]<=1.0:
									# {"feature": "Bar", "instances": 114, "metric_value": 0.4767, "depth": 9}
									if obj[8]<=2.0:
										# {"feature": "Children", "instances": 110, "metric_value": 0.4902, "depth": 10}
										if obj[5]>0:
											# {"feature": "Age", "instances": 62, "metric_value": 0.4802, "depth": 11}
											if obj[4]<=2:
												# {"feature": "Gender", "instances": 51, "metric_value": 0.4973, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 33, "metric_value": 0.4959, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 18, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[4]>2:
												# {"feature": "Gender", "instances": 11, "metric_value": 0.3879, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[5]<=0:
											# {"feature": "Age", "instances": 48, "metric_value": 0.465, "depth": 11}
											if obj[4]<=4:
												# {"feature": "Gender", "instances": 37, "metric_value": 0.4459, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 25, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 12, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[4]>4:
												# {"feature": "Gender", "instances": 11, "metric_value": 0.4935, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4898, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'False'
										else: return 'True'
									elif obj[8]>2.0:
										return 'True'
									else: return 'True'
								elif obj[10]>1.0:
									# {"feature": "Gender", "instances": 26, "metric_value": 0.4733, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Age", "instances": 18, "metric_value": 0.4375, "depth": 10}
										if obj[4]>1:
											# {"feature": "Bar", "instances": 16, "metric_value": 0.4271, "depth": 11}
											if obj[8]>1.0:
												# {"feature": "Children", "instances": 12, "metric_value": 0.4381, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4082, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[5]<=0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[8]<=1.0:
												# {"feature": "Children", "instances": 4, "metric_value": 0.25, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[4]<=1:
											return 'False'
										else: return 'False'
									elif obj[3]>0:
										# {"feature": "Age", "instances": 8, "metric_value": 0.4286, "depth": 10}
										if obj[4]>1:
											# {"feature": "Bar", "instances": 7, "metric_value": 0.4762, "depth": 11}
											if obj[8]<=1.0:
												# {"feature": "Children", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[8]>1.0:
												# {"feature": "Children", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[4]<=1:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[6]>2:
								# {"feature": "Gender", "instances": 29, "metric_value": 0.3138, "depth": 8}
								if obj[3]<=0:
									# {"feature": "Restaurant20to50", "instances": 20, "metric_value": 0.2278, "depth": 9}
									if obj[10]<=2.0:
										# {"feature": "Age", "instances": 18, "metric_value": 0.1728, "depth": 10}
										if obj[4]<=1:
											return 'True'
										elif obj[4]>1:
											# {"feature": "Children", "instances": 9, "metric_value": 0.2667, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Bar", "instances": 5, "metric_value": 0.4667, "depth": 12}
												if obj[8]<=0.0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[8]>0.0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[5]>0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[10]>2.0:
										# {"feature": "Age", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[4]<=0:
											# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[5]<=1:
												# {"feature": "Bar", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[8]<=0.0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[3]>0:
									# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.381, "depth": 9}
									if obj[10]>0.0:
										# {"feature": "Age", "instances": 7, "metric_value": 0.4762, "depth": 10}
										if obj[4]>1:
											# {"feature": "Children", "instances": 4, "metric_value": 0.3333, "depth": 11}
											if obj[5]>0:
												# {"feature": "Bar", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[8]<=0.0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[5]<=0:
												return 'False'
											else: return 'False'
										elif obj[4]<=1:
											# {"feature": "Children", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Bar", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[8]<=4.0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[10]<=0.0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[1]>2:
							# {"feature": "Restaurant20to50", "instances": 121, "metric_value": 0.4185, "depth": 7}
							if obj[10]<=1.0:
								# {"feature": "Age", "instances": 96, "metric_value": 0.4505, "depth": 8}
								if obj[4]>1:
									# {"feature": "Education", "instances": 63, "metric_value": 0.4709, "depth": 9}
									if obj[6]>0:
										# {"feature": "Bar", "instances": 38, "metric_value": 0.4848, "depth": 10}
										if obj[8]<=0.0:
											# {"feature": "Gender", "instances": 23, "metric_value": 0.4396, "depth": 11}
											if obj[3]>0:
												# {"feature": "Children", "instances": 14, "metric_value": 0.5, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 10, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]<=0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Children", "instances": 9, "metric_value": 0.2222, "depth": 12}
												if obj[5]<=0:
													return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[8]>0.0:
											# {"feature": "Children", "instances": 15, "metric_value": 0.4405, "depth": 11}
											if obj[5]>0:
												# {"feature": "Gender", "instances": 8, "metric_value": 0.3, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											elif obj[5]<=0:
												# {"feature": "Gender", "instances": 7, "metric_value": 0.3429, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]>0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[6]<=0:
										# {"feature": "Children", "instances": 25, "metric_value": 0.3994, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Gender", "instances": 17, "metric_value": 0.4566, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Bar", "instances": 14, "metric_value": 0.45, "depth": 12}
												if obj[8]<=0.0:
													# {"feature": "Direction_same", "instances": 10, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[8]>0.0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Bar", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[8]<=0.0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[5]>0:
											# {"feature": "Bar", "instances": 8, "metric_value": 0.2083, "depth": 11}
											if obj[8]<=0.0:
												# {"feature": "Gender", "instances": 6, "metric_value": 0.2667, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											elif obj[8]>0.0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[4]<=1:
									# {"feature": "Education", "instances": 33, "metric_value": 0.3284, "depth": 9}
									if obj[6]<=3:
										# {"feature": "Bar", "instances": 31, "metric_value": 0.3135, "depth": 10}
										if obj[8]<=2.0:
											# {"feature": "Gender", "instances": 25, "metric_value": 0.2667, "depth": 11}
											if obj[3]>0:
												# {"feature": "Children", "instances": 15, "metric_value": 0.2222, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 12, "metric_value": 0.2778, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Children", "instances": 10, "metric_value": 0.32, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[8]>2.0:
											# {"feature": "Gender", "instances": 6, "metric_value": 0.5, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Children", "instances": 6, "metric_value": 0.5, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[6]>3:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[10]>1.0:
								# {"feature": "Children", "instances": 25, "metric_value": 0.192, "depth": 8}
								if obj[5]<=0:
									return 'True'
								elif obj[5]>0:
									# {"feature": "Age", "instances": 10, "metric_value": 0.3, "depth": 9}
									if obj[4]>1:
										# {"feature": "Bar", "instances": 8, "metric_value": 0.3333, "depth": 10}
										if obj[8]<=3.0:
											# {"feature": "Education", "instances": 6, "metric_value": 0.25, "depth": 11}
											if obj[6]>2:
												# {"feature": "Gender", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[6]<=2:
												return 'True'
											else: return 'True'
										elif obj[8]>3.0:
											# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Education", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[6]<=2:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[4]<=1:
										return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[7]<=1.5048799563075503:
						# {"feature": "Time", "instances": 59, "metric_value": 0.3448, "depth": 6}
						if obj[1]>0:
							# {"feature": "Restaurant20to50", "instances": 45, "metric_value": 0.399, "depth": 7}
							if obj[10]>0.0:
								# {"feature": "Age", "instances": 33, "metric_value": 0.3342, "depth": 8}
								if obj[4]>2:
									# {"feature": "Children", "instances": 17, "metric_value": 0.183, "depth": 9}
									if obj[5]>0:
										# {"feature": "Gender", "instances": 9, "metric_value": 0.3457, "depth": 10}
										if obj[3]<=1:
											# {"feature": "Education", "instances": 9, "metric_value": 0.3457, "depth": 11}
											if obj[6]<=0:
												# {"feature": "Bar", "instances": 9, "metric_value": 0.3457, "depth": 12}
												if obj[8]<=0.0:
													# {"feature": "Direction_same", "instances": 9, "metric_value": 0.3457, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[5]<=0:
										return 'True'
									else: return 'True'
								elif obj[4]<=2:
									# {"feature": "Education", "instances": 16, "metric_value": 0.45, "depth": 9}
									if obj[6]<=2:
										# {"feature": "Children", "instances": 15, "metric_value": 0.4727, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Gender", "instances": 11, "metric_value": 0.404, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Bar", "instances": 9, "metric_value": 0.4444, "depth": 12}
												if obj[8]>0.0:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[8]<=0.0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[3]>0:
												return 'True'
											else: return 'True'
										elif obj[5]>0:
											# {"feature": "Gender", "instances": 4, "metric_value": 0.3333, "depth": 11}
											if obj[3]>0:
												# {"feature": "Bar", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[8]<=0.0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[3]<=0:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[6]>2:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[10]<=0.0:
								# {"feature": "Education", "instances": 12, "metric_value": 0.375, "depth": 8}
								if obj[6]<=2:
									# {"feature": "Children", "instances": 8, "metric_value": 0.3333, "depth": 9}
									if obj[5]>0:
										# {"feature": "Gender", "instances": 6, "metric_value": 0.4444, "depth": 10}
										if obj[3]>0:
											# {"feature": "Age", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[4]<=1:
												# {"feature": "Bar", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[8]<=0.0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]<=0:
											# {"feature": "Age", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[4]<=6:
												# {"feature": "Bar", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[8]<=0.0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[5]<=0:
										return 'True'
									else: return 'True'
								elif obj[6]>2:
									# {"feature": "Gender", "instances": 4, "metric_value": 0.0, "depth": 9}
									if obj[3]>0:
										return 'False'
									elif obj[3]<=0:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'True'
						elif obj[1]<=0:
							# {"feature": "Age", "instances": 14, "metric_value": 0.1224, "depth": 7}
							if obj[4]>2:
								# {"feature": "Education", "instances": 7, "metric_value": 0.2143, "depth": 8}
								if obj[6]<=0:
									# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.3333, "depth": 9}
									if obj[10]<=1.0:
										# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[3]<=1:
											# {"feature": "Children", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[5]<=1:
												# {"feature": "Bar", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[8]<=0.0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[10]>1.0:
										return 'True'
									else: return 'True'
								elif obj[6]>0:
									return 'True'
								else: return 'True'
							elif obj[4]<=2:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[12]<=1:
					# {"feature": "Occupation", "instances": 175, "metric_value": 0.4681, "depth": 5}
					if obj[7]>0:
						# {"feature": "Education", "instances": 171, "metric_value": 0.4675, "depth": 6}
						if obj[6]<=2:
							# {"feature": "Restaurant20to50", "instances": 138, "metric_value": 0.4827, "depth": 7}
							if obj[10]>0.0:
								# {"feature": "Time", "instances": 97, "metric_value": 0.4603, "depth": 8}
								if obj[1]<=3:
									# {"feature": "Children", "instances": 69, "metric_value": 0.4615, "depth": 9}
									if obj[5]<=0:
										# {"feature": "Age", "instances": 51, "metric_value": 0.4386, "depth": 10}
										if obj[4]>1:
											# {"feature": "Gender", "instances": 27, "metric_value": 0.3691, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Bar", "instances": 16, "metric_value": 0.2885, "depth": 12}
												if obj[8]<=1.0:
													# {"feature": "Direction_same", "instances": 13, "metric_value": 0.355, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[8]>1.0:
													return 'False'
												else: return 'False'
											elif obj[3]>0:
												# {"feature": "Bar", "instances": 11, "metric_value": 0.4481, "depth": 12}
												if obj[8]<=0.0:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4898, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[8]>0.0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[4]<=1:
											# {"feature": "Bar", "instances": 24, "metric_value": 0.4857, "depth": 11}
											if obj[8]>1.0:
												# {"feature": "Gender", "instances": 14, "metric_value": 0.4643, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 10, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[8]<=1.0:
												# {"feature": "Gender", "instances": 10, "metric_value": 0.4, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'False'
										else: return 'False'
									elif obj[5]>0:
										# {"feature": "Bar", "instances": 18, "metric_value": 0.381, "depth": 10}
										if obj[8]<=1.0:
											# {"feature": "Age", "instances": 14, "metric_value": 0.4286, "depth": 11}
											if obj[4]<=6:
												# {"feature": "Gender", "instances": 12, "metric_value": 0.5, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[4]>6:
												return 'True'
											else: return 'True'
										elif obj[8]>1.0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[1]>3:
									# {"feature": "Children", "instances": 28, "metric_value": 0.352, "depth": 9}
									if obj[5]>0:
										# {"feature": "Gender", "instances": 14, "metric_value": 0.2143, "depth": 10}
										if obj[3]>0:
											# {"feature": "Age", "instances": 8, "metric_value": 0.3333, "depth": 11}
											if obj[4]<=3:
												# {"feature": "Bar", "instances": 6, "metric_value": 0.1667, "depth": 12}
												if obj[8]<=0.0:
													return 'False'
												elif obj[8]>0.0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[4]>3:
												# {"feature": "Bar", "instances": 2, "metric_value": 0.0, "depth": 12}
												if obj[8]<=0.0:
													return 'True'
												elif obj[8]>0.0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[3]<=0:
											return 'False'
										else: return 'False'
									elif obj[5]<=0:
										# {"feature": "Age", "instances": 14, "metric_value": 0.3571, "depth": 10}
										if obj[4]<=4:
											# {"feature": "Gender", "instances": 10, "metric_value": 0.4762, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Bar", "instances": 7, "metric_value": 0.3429, "depth": 12}
												if obj[8]>0.0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[8]<=0.0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Bar", "instances": 3, "metric_value": 0.3333, "depth": 12}
												if obj[8]>0.0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[8]<=0.0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[4]>4:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[10]<=0.0:
								# {"feature": "Age", "instances": 41, "metric_value": 0.4671, "depth": 8}
								if obj[4]<=5:
									# {"feature": "Bar", "instances": 35, "metric_value": 0.4667, "depth": 9}
									if obj[8]<=1.0:
										# {"feature": "Gender", "instances": 30, "metric_value": 0.4143, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Children", "instances": 16, "metric_value": 0.25, "depth": 11}
											if obj[5]>0:
												# {"feature": "Time", "instances": 8, "metric_value": 0.4286, "depth": 12}
												if obj[1]<=2:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4898, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[1]>2:
													return 'False'
												else: return 'False'
											elif obj[5]<=0:
												return 'False'
											else: return 'False'
										elif obj[3]>0:
											# {"feature": "Children", "instances": 14, "metric_value": 0.449, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Time", "instances": 7, "metric_value": 0.3429, "depth": 12}
												if obj[1]<=2:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[1]>2:
													return 'True'
												else: return 'True'
											elif obj[5]>0:
												# {"feature": "Time", "instances": 7, "metric_value": 0.381, "depth": 12}
												if obj[1]<=2:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[1]>2:
													return 'False'
												else: return 'False'
											else: return 'True'
										else: return 'True'
									elif obj[8]>1.0:
										# {"feature": "Gender", "instances": 5, "metric_value": 0.0, "depth": 10}
										if obj[3]<=0:
											return 'True'
										elif obj[3]>0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[4]>5:
									# {"feature": "Time", "instances": 6, "metric_value": 0.1667, "depth": 9}
									if obj[1]>0:
										return 'True'
									elif obj[1]<=0:
										# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[5]<=1:
												# {"feature": "Bar", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[8]<=0.0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'True'
						elif obj[6]>2:
							# {"feature": "Gender", "instances": 33, "metric_value": 0.3326, "depth": 7}
							if obj[3]<=0:
								# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.2245, "depth": 8}
								if obj[10]<=1.0:
									# {"feature": "Bar", "instances": 14, "metric_value": 0.119, "depth": 9}
									if obj[8]<=0.0:
										return 'False'
									elif obj[8]>0.0:
										# {"feature": "Age", "instances": 6, "metric_value": 0.0, "depth": 10}
										if obj[4]<=1:
											return 'False'
										elif obj[4]>1:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[10]>1.0:
									# {"feature": "Time", "instances": 7, "metric_value": 0.2381, "depth": 9}
									if obj[1]>0:
										# {"feature": "Age", "instances": 6, "metric_value": 0.2222, "depth": 10}
										if obj[4]>0:
											return 'False'
										elif obj[4]<=0:
											# {"feature": "Children", "instances": 3, "metric_value": 0.0, "depth": 11}
											if obj[5]>0:
												return 'False'
											elif obj[5]<=0:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[1]<=0:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[3]>0:
								# {"feature": "Age", "instances": 12, "metric_value": 0.419, "depth": 8}
								if obj[4]<=4:
									# {"feature": "Time", "instances": 7, "metric_value": 0.3429, "depth": 9}
									if obj[1]<=2:
										# {"feature": "Children", "instances": 5, "metric_value": 0.3, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Bar", "instances": 4, "metric_value": 0.3333, "depth": 11}
											if obj[8]>0.0:
												# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=1.0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[8]<=0.0:
												return 'False'
											else: return 'False'
										elif obj[5]>0:
											return 'True'
										else: return 'True'
									elif obj[1]>2:
										return 'True'
									else: return 'True'
								elif obj[4]>4:
									# {"feature": "Time", "instances": 5, "metric_value": 0.2, "depth": 9}
									if obj[1]<=3:
										return 'False'
									elif obj[1]>3:
										# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.0, "depth": 10}
										if obj[10]>0.0:
											return 'False'
										elif obj[10]<=0.0:
											return 'True'
										else: return 'True'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[7]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[2]<=1:
		# {"feature": "Bar", "instances": 2258, "metric_value": 0.4643, "depth": 2}
		if obj[8]>0.0:
			# {"feature": "Time", "instances": 1296, "metric_value": 0.4911, "depth": 3}
			if obj[1]>0:
				# {"feature": "Passanger", "instances": 933, "metric_value": 0.4879, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Coffeehouse", "instances": 743, "metric_value": 0.4889, "depth": 5}
					if obj[9]>1.0:
						# {"feature": "Age", "instances": 409, "metric_value": 0.4914, "depth": 6}
						if obj[4]>0:
							# {"feature": "Restaurant20to50", "instances": 356, "metric_value": 0.4917, "depth": 7}
							if obj[10]<=2.0:
								# {"feature": "Children", "instances": 300, "metric_value": 0.495, "depth": 8}
								if obj[5]<=0:
									# {"feature": "Occupation", "instances": 194, "metric_value": 0.4857, "depth": 9}
									if obj[7]>5:
										# {"feature": "Direction_same", "instances": 131, "metric_value": 0.4719, "depth": 10}
										if obj[11]<=0:
											# {"feature": "Education", "instances": 116, "metric_value": 0.4648, "depth": 11}
											if obj[6]<=2:
												# {"feature": "Distance", "instances": 96, "metric_value": 0.4485, "depth": 12}
												if obj[12]<=2:
													# {"feature": "Gender", "instances": 68, "metric_value": 0.4708, "depth": 13}
													if obj[3]<=0:
														return 'True'
													elif obj[3]>0:
														return 'True'
													else: return 'True'
												elif obj[12]>2:
													# {"feature": "Gender", "instances": 28, "metric_value": 0.3158, "depth": 13}
													if obj[3]<=0:
														return 'True'
													elif obj[3]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[6]>2:
												# {"feature": "Distance", "instances": 20, "metric_value": 0.4933, "depth": 12}
												if obj[12]<=2:
													# {"feature": "Gender", "instances": 15, "metric_value": 0.4741, "depth": 13}
													if obj[3]<=0:
														return 'False'
													elif obj[3]>0:
														return 'True'
													else: return 'True'
												elif obj[12]>2:
													# {"feature": "Gender", "instances": 5, "metric_value": 0.2667, "depth": 13}
													if obj[3]<=0:
														return 'True'
													elif obj[3]>0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[11]>0:
											# {"feature": "Gender", "instances": 15, "metric_value": 0.4308, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Education", "instances": 13, "metric_value": 0.4615, "depth": 12}
												if obj[6]<=2:
													# {"feature": "Distance", "instances": 12, "metric_value": 0.4857, "depth": 13}
													if obj[12]>1:
														return 'False'
													elif obj[12]<=1:
														return 'True'
													else: return 'True'
												elif obj[6]>2:
													return 'False'
												else: return 'False'
											elif obj[3]>0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[7]<=5:
										# {"feature": "Distance", "instances": 63, "metric_value": 0.4735, "depth": 10}
										if obj[12]>1:
											# {"feature": "Gender", "instances": 38, "metric_value": 0.4729, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 23, "metric_value": 0.4497, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Education", "instances": 19, "metric_value": 0.4503, "depth": 13}
													if obj[6]<=2:
														return 'False'
													elif obj[6]>2:
														return 'False'
													else: return 'False'
												elif obj[11]>0:
													# {"feature": "Education", "instances": 4, "metric_value": 0.3333, "depth": 13}
													if obj[6]>1:
														return 'True'
													elif obj[6]<=1:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Education", "instances": 15, "metric_value": 0.4103, "depth": 12}
												if obj[6]<=3:
													# {"feature": "Direction_same", "instances": 13, "metric_value": 0.4685, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[6]>3:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[12]<=1:
											# {"feature": "Direction_same", "instances": 25, "metric_value": 0.4174, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Education", "instances": 23, "metric_value": 0.429, "depth": 12}
												if obj[6]>1:
													# {"feature": "Gender", "instances": 15, "metric_value": 0.3905, "depth": 13}
													if obj[3]<=0:
														return 'False'
													elif obj[3]>0:
														return 'False'
													else: return 'False'
												elif obj[6]<=1:
													# {"feature": "Gender", "instances": 8, "metric_value": 0.4667, "depth": 13}
													if obj[3]>0:
														return 'True'
													elif obj[3]<=0:
														return 'False'
													else: return 'False'
												else: return 'True'
											elif obj[11]>0:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[5]>0:
									# {"feature": "Direction_same", "instances": 106, "metric_value": 0.4611, "depth": 9}
									if obj[11]<=0:
										# {"feature": "Occupation", "instances": 95, "metric_value": 0.4675, "depth": 10}
										if obj[7]<=10:
											# {"feature": "Gender", "instances": 61, "metric_value": 0.4772, "depth": 11}
											if obj[3]>0:
												# {"feature": "Distance", "instances": 41, "metric_value": 0.46, "depth": 12}
												if obj[12]>1:
													# {"feature": "Education", "instances": 32, "metric_value": 0.4837, "depth": 13}
													if obj[6]<=2:
														return 'False'
													elif obj[6]>2:
														return 'False'
													else: return 'False'
												elif obj[12]<=1:
													# {"feature": "Education", "instances": 9, "metric_value": 0.3016, "depth": 13}
													if obj[6]>0:
														return 'False'
													elif obj[6]<=0:
														return 'True'
													else: return 'True'
												else: return 'False'
											elif obj[3]<=0:
												# {"feature": "Education", "instances": 20, "metric_value": 0.4421, "depth": 12}
												if obj[6]>0:
													# {"feature": "Distance", "instances": 19, "metric_value": 0.4579, "depth": 13}
													if obj[12]>1:
														return 'True'
													elif obj[12]<=1:
														return 'True'
													else: return 'True'
												elif obj[6]<=0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[7]>10:
											# {"feature": "Gender", "instances": 34, "metric_value": 0.4059, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Distance", "instances": 24, "metric_value": 0.3487, "depth": 12}
												if obj[12]>1:
													# {"feature": "Education", "instances": 17, "metric_value": 0.2353, "depth": 13}
													if obj[6]<=2:
														return 'False'
													elif obj[6]>2:
														return 'False'
													else: return 'False'
												elif obj[12]<=1:
													# {"feature": "Education", "instances": 7, "metric_value": 0.2286, "depth": 13}
													if obj[6]<=2:
														return 'False'
													elif obj[6]>2:
														return 'True'
													else: return 'True'
												else: return 'False'
											elif obj[3]>0:
												# {"feature": "Education", "instances": 10, "metric_value": 0.419, "depth": 12}
												if obj[6]>0:
													# {"feature": "Distance", "instances": 7, "metric_value": 0.381, "depth": 13}
													if obj[12]>1:
														return 'False'
													elif obj[12]<=1:
														return 'False'
													else: return 'False'
												elif obj[6]<=0:
													# {"feature": "Distance", "instances": 3, "metric_value": 0.3333, "depth": 13}
													if obj[12]<=2:
														return 'False'
													elif obj[12]>2:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'False'
										else: return 'False'
									elif obj[11]>0:
										# {"feature": "Education", "instances": 11, "metric_value": 0.1818, "depth": 10}
										if obj[6]>0:
											return 'True'
										elif obj[6]<=0:
											# {"feature": "Gender", "instances": 4, "metric_value": 0.3333, "depth": 11}
											if obj[3]>0:
												# {"feature": "Distance", "instances": 3, "metric_value": 0.0, "depth": 12}
												if obj[12]<=1:
													return 'False'
												elif obj[12]>1:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												return 'True'
											else: return 'True'
										else: return 'False'
									else: return 'True'
								else: return 'False'
							elif obj[10]>2.0:
								# {"feature": "Gender", "instances": 56, "metric_value": 0.3957, "depth": 8}
								if obj[3]<=0:
									# {"feature": "Education", "instances": 31, "metric_value": 0.2804, "depth": 9}
									if obj[6]<=3:
										# {"feature": "Distance", "instances": 20, "metric_value": 0.1667, "depth": 10}
										if obj[12]>1:
											# {"feature": "Children", "instances": 12, "metric_value": 0.25, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Occupation", "instances": 8, "metric_value": 0.3333, "depth": 12}
												if obj[7]>5:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.3333, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[7]<=5:
													return 'True'
												else: return 'True'
											elif obj[5]>0:
												return 'True'
											else: return 'True'
										elif obj[12]<=1:
											return 'True'
										else: return 'True'
									elif obj[6]>3:
										# {"feature": "Distance", "instances": 11, "metric_value": 0.3636, "depth": 10}
										if obj[12]<=2:
											# {"feature": "Direction_same", "instances": 8, "metric_value": 0.4667, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Occupation", "instances": 5, "metric_value": 0.3, "depth": 12}
												if obj[7]<=1:
													# {"feature": "Children", "instances": 4, "metric_value": 0.3333, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												elif obj[7]>1:
													return 'False'
												else: return 'False'
											elif obj[11]>0:
												# {"feature": "Occupation", "instances": 3, "metric_value": 0.0, "depth": 12}
												if obj[7]<=1:
													return 'False'
												elif obj[7]>1:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[12]>2:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[3]>0:
									# {"feature": "Education", "instances": 25, "metric_value": 0.4255, "depth": 9}
									if obj[6]<=3:
										# {"feature": "Occupation", "instances": 22, "metric_value": 0.4136, "depth": 10}
										if obj[7]<=10:
											# {"feature": "Children", "instances": 20, "metric_value": 0.3859, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Distance", "instances": 11, "metric_value": 0.2182, "depth": 12}
												if obj[12]>1:
													return 'False'
												elif obj[12]<=1:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.4667, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												else: return 'False'
											elif obj[5]>0:
												# {"feature": "Distance", "instances": 9, "metric_value": 0.4889, "depth": 12}
												if obj[12]<=1:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[12]>1:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[7]>10:
											return 'True'
										else: return 'True'
									elif obj[6]>3:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'True'
						elif obj[4]<=0:
							# {"feature": "Education", "instances": 53, "metric_value": 0.3565, "depth": 7}
							if obj[6]<=2:
								# {"feature": "Restaurant20to50", "instances": 34, "metric_value": 0.4524, "depth": 8}
								if obj[10]<=2.0:
									# {"feature": "Occupation", "instances": 28, "metric_value": 0.4615, "depth": 9}
									if obj[7]>1:
										# {"feature": "Direction_same", "instances": 26, "metric_value": 0.4861, "depth": 10}
										if obj[11]<=0:
											# {"feature": "Distance", "instances": 23, "metric_value": 0.4752, "depth": 11}
											if obj[12]>1:
												# {"feature": "Children", "instances": 16, "metric_value": 0.4643, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Gender", "instances": 9, "metric_value": 0.3333, "depth": 13}
													if obj[3]>0:
														return 'False'
													elif obj[3]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Gender", "instances": 7, "metric_value": 0.3429, "depth": 13}
													if obj[3]>0:
														return 'True'
													elif obj[3]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[12]<=1:
												# {"feature": "Gender", "instances": 7, "metric_value": 0.4762, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Children", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[5]<=0:
														return 'False'
													elif obj[5]>0:
														return 'False'
													else: return 'False'
												elif obj[3]>0:
													# {"feature": "Children", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[5]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[11]>0:
											# {"feature": "Gender", "instances": 3, "metric_value": 0.3333, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[12]<=1:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]>0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[7]<=1:
										return 'False'
									else: return 'False'
								elif obj[10]>2.0:
									# {"feature": "Occupation", "instances": 6, "metric_value": 0.1667, "depth": 9}
									if obj[7]<=5:
										return 'True'
									elif obj[7]>5:
										# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[12]<=1:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[6]>2:
								# {"feature": "Occupation", "instances": 19, "metric_value": 0.0877, "depth": 8}
								if obj[7]<=16:
									return 'False'
								elif obj[7]>16:
									# {"feature": "Direction_same", "instances": 6, "metric_value": 0.25, "depth": 9}
									if obj[11]<=0:
										# {"feature": "Distance", "instances": 4, "metric_value": 0.3333, "depth": 10}
										if obj[12]>1:
											# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Children", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[5]<=1:
													# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[10]<=1.0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[12]<=1:
											return 'False'
										else: return 'False'
									elif obj[11]>0:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[9]<=1.0:
						# {"feature": "Education", "instances": 334, "metric_value": 0.4654, "depth": 6}
						if obj[6]>0:
							# {"feature": "Restaurant20to50", "instances": 219, "metric_value": 0.4311, "depth": 7}
							if obj[10]<=2.0:
								# {"feature": "Age", "instances": 215, "metric_value": 0.432, "depth": 8}
								if obj[4]<=4:
									# {"feature": "Occupation", "instances": 168, "metric_value": 0.4429, "depth": 9}
									if obj[7]>5:
										# {"feature": "Distance", "instances": 120, "metric_value": 0.408, "depth": 10}
										if obj[12]>1:
											# {"feature": "Gender", "instances": 68, "metric_value": 0.446, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 43, "metric_value": 0.4894, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Children", "instances": 37, "metric_value": 0.4967, "depth": 13}
													if obj[5]<=0:
														return 'False'
													elif obj[5]>0:
														return 'False'
													else: return 'False'
												elif obj[11]>0:
													# {"feature": "Children", "instances": 6, "metric_value": 0.4167, "depth": 13}
													if obj[5]<=0:
														return 'False'
													elif obj[5]>0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 25, "metric_value": 0.3429, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Children", "instances": 21, "metric_value": 0.4066, "depth": 13}
													if obj[5]<=0:
														return 'False'
													elif obj[5]>0:
														return 'False'
													else: return 'False'
												elif obj[11]>0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[12]<=1:
											# {"feature": "Gender", "instances": 52, "metric_value": 0.3207, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 28, "metric_value": 0.4011, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Children", "instances": 26, "metric_value": 0.3932, "depth": 13}
													if obj[5]<=0:
														return 'False'
													elif obj[5]>0:
														return 'False'
													else: return 'False'
												elif obj[11]>0:
													# {"feature": "Children", "instances": 2, "metric_value": 0.0, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'False'
													else: return 'False'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Children", "instances": 24, "metric_value": 0.2125, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 20, "metric_value": 0.25, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												elif obj[5]>0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[7]<=5:
										# {"feature": "Direction_same", "instances": 48, "metric_value": 0.4791, "depth": 10}
										if obj[11]<=0:
											# {"feature": "Gender", "instances": 43, "metric_value": 0.4659, "depth": 11}
											if obj[3]>0:
												# {"feature": "Children", "instances": 23, "metric_value": 0.3819, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Distance", "instances": 17, "metric_value": 0.3258, "depth": 13}
													if obj[12]<=2:
														return 'True'
													elif obj[12]>2:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Distance", "instances": 6, "metric_value": 0.4167, "depth": 13}
													if obj[12]>1:
														return 'False'
													elif obj[12]<=1:
														return 'True'
													else: return 'True'
												else: return 'False'
											elif obj[3]<=0:
												# {"feature": "Distance", "instances": 20, "metric_value": 0.4, "depth": 12}
												if obj[12]<=2:
													# {"feature": "Children", "instances": 16, "metric_value": 0.4583, "depth": 13}
													if obj[5]<=0:
														return 'False'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												elif obj[12]>2:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[11]>0:
											# {"feature": "Gender", "instances": 5, "metric_value": 0.0, "depth": 11}
											if obj[3]>0:
												return 'False'
											elif obj[3]<=0:
												return 'True'
											else: return 'True'
										else: return 'False'
									else: return 'True'
								elif obj[4]>4:
									# {"feature": "Children", "instances": 47, "metric_value": 0.3124, "depth": 9}
									if obj[5]>0:
										# {"feature": "Occupation", "instances": 34, "metric_value": 0.2189, "depth": 10}
										if obj[7]<=12:
											# {"feature": "Distance", "instances": 21, "metric_value": 0.0762, "depth": 11}
											if obj[12]<=2:
												return 'False'
											elif obj[12]>2:
												# {"feature": "Gender", "instances": 5, "metric_value": 0.2667, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]>0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[7]>12:
											# {"feature": "Direction_same", "instances": 13, "metric_value": 0.3462, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Gender", "instances": 12, "metric_value": 0.3125, "depth": 12}
												if obj[3]>0:
													# {"feature": "Distance", "instances": 8, "metric_value": 0.4583, "depth": 13}
													if obj[12]<=2:
														return 'False'
													elif obj[12]>2:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													return 'False'
												else: return 'False'
											elif obj[11]>0:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[5]<=0:
										# {"feature": "Gender", "instances": 13, "metric_value": 0.2198, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Distance", "instances": 7, "metric_value": 0.3429, "depth": 11}
											if obj[12]<=1:
												# {"feature": "Occupation", "instances": 5, "metric_value": 0.3, "depth": 12}
												if obj[7]<=5:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[7]>5:
													return 'False'
												else: return 'False'
											elif obj[12]>1:
												return 'True'
											else: return 'True'
										elif obj[3]>0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[10]>2.0:
								return 'True'
							else: return 'True'
						elif obj[6]<=0:
							# {"feature": "Age", "instances": 115, "metric_value": 0.4784, "depth": 7}
							if obj[4]>0:
								# {"feature": "Restaurant20to50", "instances": 66, "metric_value": 0.4579, "depth": 8}
								if obj[10]<=1.0:
									# {"feature": "Occupation", "instances": 48, "metric_value": 0.4419, "depth": 9}
									if obj[7]<=15:
										# {"feature": "Distance", "instances": 43, "metric_value": 0.4389, "depth": 10}
										if obj[12]>1:
											# {"feature": "Gender", "instances": 30, "metric_value": 0.4242, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 22, "metric_value": 0.3818, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Children", "instances": 20, "metric_value": 0.42, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												elif obj[11]>0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Children", "instances": 8, "metric_value": 0.5, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[12]<=1:
											# {"feature": "Children", "instances": 13, "metric_value": 0.3919, "depth": 11}
											if obj[5]>0:
												# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4286, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Gender", "instances": 6, "metric_value": 0.5, "depth": 13}
													if obj[3]<=0:
														return 'True'
													elif obj[3]>0:
														return 'False'
													else: return 'False'
												elif obj[11]>0:
													return 'False'
												else: return 'False'
											elif obj[5]<=0:
												# {"feature": "Gender", "instances": 6, "metric_value": 0.2222, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[7]>15:
										return 'False'
									else: return 'False'
								elif obj[10]>1.0:
									# {"feature": "Gender", "instances": 18, "metric_value": 0.2667, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Children", "instances": 10, "metric_value": 0.4, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Distance", "instances": 9, "metric_value": 0.4, "depth": 11}
											if obj[12]>1:
												# {"feature": "Occupation", "instances": 5, "metric_value": 0.2, "depth": 12}
												if obj[7]<=7:
													return 'True'
												elif obj[7]>7:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.0, "depth": 13}
													if obj[11]>0:
														return 'True'
													elif obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'True'
											elif obj[12]<=1:
												# {"feature": "Occupation", "instances": 4, "metric_value": 0.0, "depth": 12}
												if obj[7]>7:
													return 'True'
												elif obj[7]<=7:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[5]>0:
											return 'False'
										else: return 'False'
									elif obj[3]>0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[4]<=0:
								# {"feature": "Children", "instances": 49, "metric_value": 0.4334, "depth": 8}
								if obj[5]<=0:
									# {"feature": "Occupation", "instances": 33, "metric_value": 0.4628, "depth": 9}
									if obj[7]>2:
										# {"feature": "Restaurant20to50", "instances": 22, "metric_value": 0.4762, "depth": 10}
										if obj[10]<=1.0:
											# {"feature": "Distance", "instances": 21, "metric_value": 0.4893, "depth": 11}
											if obj[12]<=2:
												# {"feature": "Gender", "instances": 16, "metric_value": 0.4896, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 12, "metric_value": 0.4242, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.3333, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[12]>2:
												# {"feature": "Gender", "instances": 5, "metric_value": 0.4667, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[10]>1.0:
											return 'True'
										else: return 'True'
									elif obj[7]<=2:
										# {"feature": "Direction_same", "instances": 11, "metric_value": 0.2909, "depth": 10}
										if obj[11]<=0:
											# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.2857, "depth": 11}
											if obj[10]>0.0:
												# {"feature": "Gender", "instances": 7, "metric_value": 0.2381, "depth": 12}
												if obj[3]>0:
													# {"feature": "Distance", "instances": 6, "metric_value": 0.1667, "depth": 13}
													if obj[12]<=2:
														return 'False'
													elif obj[12]>2:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											elif obj[10]<=0.0:
												return 'False'
											else: return 'False'
										elif obj[11]>0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[5]>0:
									# {"feature": "Distance", "instances": 16, "metric_value": 0.2885, "depth": 9}
									if obj[12]>1:
										# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.3357, "depth": 10}
										if obj[10]>-1.0:
											# {"feature": "Gender", "instances": 11, "metric_value": 0.3879, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4167, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Occupation", "instances": 4, "metric_value": 0.25, "depth": 13}
													if obj[7]<=18:
														return 'False'
													elif obj[7]>18:
														return 'True'
													else: return 'True'
												elif obj[11]>0:
													# {"feature": "Occupation", "instances": 2, "metric_value": 0.0, "depth": 13}
													if obj[7]>18:
														return 'False'
													elif obj[7]<=18:
														return 'True'
													else: return 'True'
												else: return 'False'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.3, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Occupation", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[7]<=3:
														return 'False'
													else: return 'False'
												elif obj[11]>0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[10]<=-1.0:
											return 'False'
										else: return 'False'
									elif obj[12]<=1:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[0]>2:
					# {"feature": "Occupation", "instances": 190, "metric_value": 0.4413, "depth": 5}
					if obj[7]<=19.70715618872958:
						# {"feature": "Coffeehouse", "instances": 179, "metric_value": 0.4572, "depth": 6}
						if obj[9]>1.0:
							# {"feature": "Age", "instances": 98, "metric_value": 0.4135, "depth": 7}
							if obj[4]<=4:
								# {"feature": "Restaurant20to50", "instances": 81, "metric_value": 0.3549, "depth": 8}
								if obj[10]<=3.0:
									# {"feature": "Gender", "instances": 78, "metric_value": 0.3323, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Education", "instances": 42, "metric_value": 0.1855, "depth": 10}
										if obj[6]<=2:
											# {"feature": "Distance", "instances": 27, "metric_value": 0.0707, "depth": 11}
											if obj[12]>1:
												# {"feature": "Children", "instances": 22, "metric_value": 0.0864, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 20, "metric_value": 0.095, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													return 'True'
												else: return 'True'
											elif obj[12]<=1:
												return 'True'
											else: return 'True'
										elif obj[6]>2:
											# {"feature": "Children", "instances": 15, "metric_value": 0.3643, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Distance", "instances": 8, "metric_value": 0.375, "depth": 12}
												if obj[12]>1:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[12]<=1:
													return 'True'
												else: return 'True'
											elif obj[5]>0:
												# {"feature": "Direction_same", "instances": 7, "metric_value": 0.2449, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 7, "metric_value": 0.2449, "depth": 13}
													if obj[12]<=2:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[3]>0:
										# {"feature": "Children", "instances": 36, "metric_value": 0.4506, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Education", "instances": 18, "metric_value": 0.2469, "depth": 11}
											if obj[6]<=1:
												return 'True'
											elif obj[6]>1:
												# {"feature": "Distance", "instances": 9, "metric_value": 0.4921, "depth": 12}
												if obj[12]>1:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4898, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[12]<=1:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[5]>0:
											# {"feature": "Education", "instances": 18, "metric_value": 0.4416, "depth": 11}
											if obj[6]<=2:
												# {"feature": "Direction_same", "instances": 11, "metric_value": 0.4628, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 11, "metric_value": 0.4628, "depth": 13}
													if obj[12]<=2:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[6]>2:
												# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4082, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 7, "metric_value": 0.4082, "depth": 13}
													if obj[12]<=2:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[10]>3.0:
									return 'False'
								else: return 'False'
							elif obj[4]>4:
								# {"feature": "Education", "instances": 17, "metric_value": 0.2647, "depth": 8}
								if obj[6]>0:
									# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.2593, "depth": 9}
									if obj[10]>1.0:
										# {"feature": "Gender", "instances": 9, "metric_value": 0.1778, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Children", "instances": 5, "metric_value": 0.2, "depth": 11}
											if obj[5]>0:
												return 'True'
											elif obj[5]<=0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[12]<=2:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[3]>0:
											return 'True'
										else: return 'True'
									elif obj[10]<=1.0:
										# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[3]<=1:
											# {"feature": "Children", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[12]<=2:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[6]<=0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[9]<=1.0:
							# {"feature": "Children", "instances": 81, "metric_value": 0.4654, "depth": 7}
							if obj[5]<=0:
								# {"feature": "Restaurant20to50", "instances": 60, "metric_value": 0.4242, "depth": 8}
								if obj[10]<=1.0:
									# {"feature": "Age", "instances": 44, "metric_value": 0.4721, "depth": 9}
									if obj[4]<=2:
										# {"feature": "Education", "instances": 32, "metric_value": 0.4597, "depth": 10}
										if obj[6]<=3:
											# {"feature": "Distance", "instances": 31, "metric_value": 0.4645, "depth": 11}
											if obj[12]>1:
												# {"feature": "Gender", "instances": 30, "metric_value": 0.48, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 20, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 10, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[12]<=1:
												return 'True'
											else: return 'True'
										elif obj[6]>3:
											return 'False'
										else: return 'False'
									elif obj[4]>2:
										# {"feature": "Education", "instances": 12, "metric_value": 0.3636, "depth": 10}
										if obj[6]<=2:
											# {"feature": "Distance", "instances": 11, "metric_value": 0.3697, "depth": 11}
											if obj[12]<=1:
												# {"feature": "Gender", "instances": 6, "metric_value": 0.2667, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]>0:
													return 'False'
												else: return 'False'
											elif obj[12]>1:
												# {"feature": "Gender", "instances": 5, "metric_value": 0.48, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[6]>2:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[10]>1.0:
									# {"feature": "Education", "instances": 16, "metric_value": 0.1987, "depth": 9}
									if obj[6]<=2:
										# {"feature": "Age", "instances": 13, "metric_value": 0.1319, "depth": 10}
										if obj[4]>2:
											# {"feature": "Distance", "instances": 7, "metric_value": 0.2143, "depth": 11}
											if obj[12]>1:
												# {"feature": "Gender", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[12]<=1:
												return 'True'
											else: return 'True'
										elif obj[4]<=2:
											return 'True'
										else: return 'True'
									elif obj[6]>2:
										# {"feature": "Age", "instances": 3, "metric_value": 0.3333, "depth": 10}
										if obj[4]<=2:
											# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[12]<=2:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[4]>2:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[5]>0:
								# {"feature": "Education", "instances": 21, "metric_value": 0.3878, "depth": 8}
								if obj[6]>0:
									# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.3, "depth": 9}
									if obj[10]<=1.0:
										# {"feature": "Age", "instances": 10, "metric_value": 0.3667, "depth": 10}
										if obj[4]<=3:
											# {"feature": "Gender", "instances": 6, "metric_value": 0.1667, "depth": 11}
											if obj[3]>0:
												return 'False'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[12]<=2:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[4]>3:
											# {"feature": "Gender", "instances": 4, "metric_value": 0.3333, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[12]<=2:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]<=0:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[10]>1.0:
										return 'False'
									else: return 'False'
								elif obj[6]<=0:
									# {"feature": "Age", "instances": 7, "metric_value": 0.3429, "depth": 9}
									if obj[4]<=2:
										# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.2667, "depth": 10}
										if obj[10]>1.0:
											# {"feature": "Gender", "instances": 3, "metric_value": 0.3333, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[12]<=2:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]<=0:
												return 'True'
											else: return 'True'
										elif obj[10]<=1.0:
											return 'False'
										else: return 'False'
									elif obj[4]>2:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'True'
					elif obj[7]>19.70715618872958:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[1]<=0:
				# {"feature": "Passanger", "instances": 363, "metric_value": 0.4495, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Distance", "instances": 333, "metric_value": 0.4386, "depth": 5}
					if obj[12]<=1:
						# {"feature": "Restaurant20to50", "instances": 170, "metric_value": 0.3751, "depth": 6}
						if obj[10]<=1.0:
							# {"feature": "Coffeehouse", "instances": 102, "metric_value": 0.4339, "depth": 7}
							if obj[9]<=2.0:
								# {"feature": "Occupation", "instances": 81, "metric_value": 0.4508, "depth": 8}
								if obj[7]>5:
									# {"feature": "Age", "instances": 50, "metric_value": 0.4506, "depth": 9}
									if obj[4]<=5:
										# {"feature": "Education", "instances": 44, "metric_value": 0.46, "depth": 10}
										if obj[6]<=3:
											# {"feature": "Children", "instances": 42, "metric_value": 0.4695, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Gender", "instances": 31, "metric_value": 0.4744, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 23, "metric_value": 0.4764, "depth": 13}
													if obj[11]<=1:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.4688, "depth": 13}
													if obj[11]<=1:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[5]>0:
												# {"feature": "Gender", "instances": 11, "metric_value": 0.3939, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.375, "depth": 13}
													if obj[11]<=1:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=1:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[6]>3:
											return 'True'
										else: return 'True'
									elif obj[4]>5:
										# {"feature": "Children", "instances": 6, "metric_value": 0.0, "depth": 10}
										if obj[5]>0:
											return 'False'
										elif obj[5]<=0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[7]<=5:
									# {"feature": "Gender", "instances": 31, "metric_value": 0.3452, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Age", "instances": 16, "metric_value": 0.15, "depth": 10}
										if obj[4]>0:
											return 'True'
										elif obj[4]<=0:
											# {"feature": "Education", "instances": 5, "metric_value": 0.0, "depth": 11}
											if obj[6]<=1:
												return 'True'
											elif obj[6]>1:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[3]>0:
										# {"feature": "Age", "instances": 15, "metric_value": 0.32, "depth": 10}
										if obj[4]>1:
											# {"feature": "Education", "instances": 10, "metric_value": 0.4, "depth": 11}
											if obj[6]<=3:
												# {"feature": "Children", "instances": 9, "metric_value": 0.4333, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[11]<=1:
														return 'False'
													else: return 'False'
												elif obj[5]<=0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=1:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[6]>3:
												return 'True'
											else: return 'True'
										elif obj[4]<=1:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[9]>2.0:
								# {"feature": "Education", "instances": 21, "metric_value": 0.2721, "depth": 8}
								if obj[6]>1:
									# {"feature": "Age", "instances": 14, "metric_value": 0.3175, "depth": 9}
									if obj[4]>3:
										# {"feature": "Occupation", "instances": 9, "metric_value": 0.381, "depth": 10}
										if obj[7]>1:
											# {"feature": "Gender", "instances": 7, "metric_value": 0.4048, "depth": 11}
											if obj[3]>0:
												# {"feature": "Children", "instances": 4, "metric_value": 0.3333, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=1:
														return 'False'
													else: return 'False'
												elif obj[5]>0:
													return 'False'
												else: return 'False'
											elif obj[3]<=0:
												# {"feature": "Children", "instances": 3, "metric_value": 0.3333, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=1:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[7]<=1:
											return 'True'
										else: return 'True'
									elif obj[4]<=3:
										return 'True'
									else: return 'True'
								elif obj[6]<=1:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[10]>1.0:
							# {"feature": "Education", "instances": 68, "metric_value": 0.2603, "depth": 7}
							if obj[6]>1:
								# {"feature": "Occupation", "instances": 40, "metric_value": 0.1636, "depth": 8}
								if obj[7]>8:
									# {"feature": "Coffeehouse", "instances": 22, "metric_value": 0.2773, "depth": 9}
									if obj[9]<=3.0:
										# {"feature": "Children", "instances": 20, "metric_value": 0.2182, "depth": 10}
										if obj[5]>0:
											# {"feature": "Age", "instances": 11, "metric_value": 0.2727, "depth": 11}
											if obj[4]<=6:
												# {"feature": "Gender", "instances": 6, "metric_value": 0.4444, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=1:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=1:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[4]>6:
												return 'True'
											else: return 'True'
										elif obj[5]<=0:
											return 'True'
										else: return 'True'
									elif obj[9]>3.0:
										# {"feature": "Age", "instances": 2, "metric_value": 0.0, "depth": 10}
										if obj[4]<=2:
											return 'False'
										elif obj[4]>2:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[7]<=8:
									return 'True'
								else: return 'True'
							elif obj[6]<=1:
								# {"feature": "Occupation", "instances": 28, "metric_value": 0.2313, "depth": 8}
								if obj[7]>5:
									# {"feature": "Age", "instances": 21, "metric_value": 0.1481, "depth": 9}
									if obj[4]<=2:
										return 'True'
									elif obj[4]>2:
										# {"feature": "Children", "instances": 9, "metric_value": 0.3016, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.2143, "depth": 11}
											if obj[9]>1.0:
												# {"feature": "Gender", "instances": 4, "metric_value": 0.3333, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=1:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											elif obj[9]<=1.0:
												return 'True'
											else: return 'True'
										elif obj[5]>0:
											# {"feature": "Coffeehouse", "instances": 2, "metric_value": 0.0, "depth": 11}
											if obj[9]<=1.0:
												return 'False'
											elif obj[9]>1.0:
												return 'True'
											else: return 'True'
										else: return 'False'
									else: return 'True'
								elif obj[7]<=5:
									# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.2381, "depth": 9}
									if obj[9]<=2.0:
										# {"feature": "Gender", "instances": 6, "metric_value": 0.2222, "depth": 10}
										if obj[3]<=0:
											return 'False'
										elif obj[3]>0:
											# {"feature": "Age", "instances": 3, "metric_value": 0.0, "depth": 11}
											if obj[4]<=1:
												return 'False'
											elif obj[4]>1:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[9]>2.0:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					elif obj[12]>1:
						# {"feature": "Restaurant20to50", "instances": 163, "metric_value": 0.4737, "depth": 6}
						if obj[10]>0.0:
							# {"feature": "Education", "instances": 140, "metric_value": 0.4638, "depth": 7}
							if obj[6]<=3:
								# {"feature": "Direction_same", "instances": 130, "metric_value": 0.475, "depth": 8}
								if obj[11]<=0:
									# {"feature": "Children", "instances": 128, "metric_value": 0.475, "depth": 9}
									if obj[5]<=0:
										# {"feature": "Occupation", "instances": 90, "metric_value": 0.4376, "depth": 10}
										if obj[7]<=10:
											# {"feature": "Age", "instances": 70, "metric_value": 0.4695, "depth": 11}
											if obj[4]>2:
												# {"feature": "Coffeehouse", "instances": 43, "metric_value": 0.4469, "depth": 12}
												if obj[9]<=3.0:
													# {"feature": "Gender", "instances": 37, "metric_value": 0.4301, "depth": 13}
													if obj[3]<=0:
														return 'True'
													elif obj[3]>0:
														return 'True'
													else: return 'True'
												elif obj[9]>3.0:
													# {"feature": "Gender", "instances": 6, "metric_value": 0.4444, "depth": 13}
													if obj[3]<=0:
														return 'False'
													elif obj[3]>0:
														return 'True'
													else: return 'True'
												else: return 'False'
											elif obj[4]<=2:
												# {"feature": "Coffeehouse", "instances": 27, "metric_value": 0.4614, "depth": 12}
												if obj[9]>0.0:
													# {"feature": "Gender", "instances": 23, "metric_value": 0.474, "depth": 13}
													if obj[3]>0:
														return 'False'
													elif obj[3]<=0:
														return 'False'
													else: return 'False'
												elif obj[9]<=0.0:
													# {"feature": "Gender", "instances": 4, "metric_value": 0.3333, "depth": 13}
													if obj[3]<=0:
														return 'True'
													elif obj[3]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[7]>10:
											# {"feature": "Age", "instances": 20, "metric_value": 0.1789, "depth": 11}
											if obj[4]>0:
												# {"feature": "Coffeehouse", "instances": 19, "metric_value": 0.182, "depth": 12}
												if obj[9]>0.0:
													# {"feature": "Gender", "instances": 14, "metric_value": 0.125, "depth": 13}
													if obj[3]<=0:
														return 'True'
													elif obj[3]>0:
														return 'True'
													else: return 'True'
												elif obj[9]<=0.0:
													# {"feature": "Gender", "instances": 5, "metric_value": 0.0, "depth": 13}
													if obj[3]<=0:
														return 'True'
													elif obj[3]>0:
														return 'False'
													else: return 'False'
												else: return 'True'
											elif obj[4]<=0:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[5]>0:
										# {"feature": "Occupation", "instances": 38, "metric_value": 0.4579, "depth": 10}
										if obj[7]>4:
											# {"feature": "Age", "instances": 27, "metric_value": 0.388, "depth": 11}
											if obj[4]>1:
												# {"feature": "Coffeehouse", "instances": 21, "metric_value": 0.4333, "depth": 12}
												if obj[9]>0.0:
													# {"feature": "Gender", "instances": 16, "metric_value": 0.4643, "depth": 13}
													if obj[3]<=0:
														return 'False'
													elif obj[3]>0:
														return 'False'
													else: return 'False'
												elif obj[9]<=0.0:
													# {"feature": "Gender", "instances": 5, "metric_value": 0.2667, "depth": 13}
													if obj[3]<=0:
														return 'True'
													elif obj[3]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[4]<=1:
												return 'True'
											else: return 'True'
										elif obj[7]<=4:
											# {"feature": "Age", "instances": 11, "metric_value": 0.3409, "depth": 11}
											if obj[4]>2:
												# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.3667, "depth": 12}
												if obj[9]>2.0:
													# {"feature": "Gender", "instances": 5, "metric_value": 0.2667, "depth": 13}
													if obj[3]>0:
														return 'False'
													elif obj[3]<=0:
														return 'False'
													else: return 'False'
												elif obj[9]<=2.0:
													# {"feature": "Gender", "instances": 3, "metric_value": 0.3333, "depth": 13}
													if obj[3]>0:
														return 'True'
													elif obj[3]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[4]<=2:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[11]>0:
									return 'False'
								else: return 'False'
							elif obj[6]>3:
								# {"feature": "Coffeehouse", "instances": 10, "metric_value": 0.1333, "depth": 8}
								if obj[9]>0.0:
									return 'True'
								elif obj[9]<=0.0:
									# {"feature": "Gender", "instances": 3, "metric_value": 0.3333, "depth": 9}
									if obj[3]>0:
										# {"feature": "Age", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[4]<=1:
											# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Occupation", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[7]<=2:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
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
						elif obj[10]<=0.0:
							# {"feature": "Gender", "instances": 23, "metric_value": 0.4007, "depth": 7}
							if obj[3]<=0:
								# {"feature": "Education", "instances": 15, "metric_value": 0.4103, "depth": 8}
								if obj[6]<=3:
									# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.337, "depth": 9}
									if obj[9]<=2.0:
										# {"feature": "Occupation", "instances": 7, "metric_value": 0.1429, "depth": 10}
										if obj[7]>3:
											return 'False'
										elif obj[7]<=3:
											# {"feature": "Age", "instances": 2, "metric_value": 0.0, "depth": 11}
											if obj[4]<=0:
												return 'False'
											elif obj[4]>0:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[9]>2.0:
										# {"feature": "Occupation", "instances": 6, "metric_value": 0.2222, "depth": 10}
										if obj[7]<=5:
											# {"feature": "Direction_same", "instances": 3, "metric_value": 0.0, "depth": 11}
											if obj[11]<=0:
												return 'False'
											elif obj[11]>0:
												return 'True'
											else: return 'True'
										elif obj[7]>5:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[6]>3:
									return 'True'
								else: return 'True'
							elif obj[3]>0:
								# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.1667, "depth": 8}
								if obj[9]<=1.0:
									return 'False'
								elif obj[9]>1.0:
									# {"feature": "Occupation", "instances": 3, "metric_value": 0.0, "depth": 9}
									if obj[7]<=10:
										return 'False'
									elif obj[7]>10:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[0]>1:
					# {"feature": "Restaurant20to50", "instances": 30, "metric_value": 0.35, "depth": 5}
					if obj[10]>0.0:
						# {"feature": "Age", "instances": 28, "metric_value": 0.3056, "depth": 6}
						if obj[4]<=3:
							# {"feature": "Coffeehouse", "instances": 18, "metric_value": 0.3819, "depth": 7}
							if obj[9]<=3.0:
								# {"feature": "Occupation", "instances": 16, "metric_value": 0.3646, "depth": 8}
								if obj[7]<=14:
									# {"feature": "Education", "instances": 12, "metric_value": 0.3704, "depth": 9}
									if obj[6]<=2:
										# {"feature": "Children", "instances": 9, "metric_value": 0.4444, "depth": 10}
										if obj[5]>0:
											# {"feature": "Distance", "instances": 8, "metric_value": 0.4286, "depth": 11}
											if obj[12]>1:
												# {"feature": "Gender", "instances": 7, "metric_value": 0.4286, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											elif obj[12]<=1:
												return 'False'
											else: return 'False'
										elif obj[5]<=0:
											return 'True'
										else: return 'True'
									elif obj[6]>2:
										return 'False'
									else: return 'False'
								elif obj[7]>14:
									return 'False'
								else: return 'False'
							elif obj[9]>3.0:
								return 'True'
							else: return 'True'
						elif obj[4]>3:
							return 'False'
						else: return 'False'
					elif obj[10]<=0.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		elif obj[8]<=0.0:
			# {"feature": "Restaurant20to50", "instances": 962, "metric_value": 0.4124, "depth": 3}
			if obj[10]<=2.0:
				# {"feature": "Children", "instances": 914, "metric_value": 0.4015, "depth": 4}
				if obj[5]>0:
					# {"feature": "Education", "instances": 480, "metric_value": 0.3487, "depth": 5}
					if obj[6]<=4:
						# {"feature": "Time", "instances": 475, "metric_value": 0.3428, "depth": 6}
						if obj[1]<=3:
							# {"feature": "Distance", "instances": 413, "metric_value": 0.3627, "depth": 7}
							if obj[12]<=2:
								# {"feature": "Coffeehouse", "instances": 321, "metric_value": 0.3987, "depth": 8}
								if obj[9]<=3.0:
									# {"feature": "Occupation", "instances": 295, "metric_value": 0.4165, "depth": 9}
									if obj[7]<=5:
										# {"feature": "Age", "instances": 150, "metric_value": 0.3717, "depth": 10}
										if obj[4]>0:
											# {"feature": "Direction_same", "instances": 130, "metric_value": 0.3499, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Passanger", "instances": 95, "metric_value": 0.3194, "depth": 12}
												if obj[0]>1:
													# {"feature": "Gender", "instances": 59, "metric_value": 0.3021, "depth": 13}
													if obj[3]>0:
														return 'False'
													elif obj[3]<=0:
														return 'False'
													else: return 'False'
												elif obj[0]<=1:
													# {"feature": "Gender", "instances": 36, "metric_value": 0.3444, "depth": 13}
													if obj[3]>0:
														return 'False'
													elif obj[3]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[11]>0:
												# {"feature": "Passanger", "instances": 35, "metric_value": 0.398, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Gender", "instances": 28, "metric_value": 0.3478, "depth": 13}
													if obj[3]>0:
														return 'False'
													elif obj[3]<=0:
														return 'False'
													else: return 'False'
												elif obj[0]>1:
													# {"feature": "Gender", "instances": 7, "metric_value": 0.4286, "depth": 13}
													if obj[3]>0:
														return 'False'
													elif obj[3]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[4]<=0:
											# {"feature": "Passanger", "instances": 20, "metric_value": 0.46, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 10, "metric_value": 0.4167, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Gender", "instances": 6, "metric_value": 0.4444, "depth": 13}
													if obj[3]<=1:
														return 'True'
													else: return 'True'
												elif obj[11]>0:
													# {"feature": "Gender", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[3]<=1:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[0]>1:
												# {"feature": "Direction_same", "instances": 10, "metric_value": 0.3111, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Gender", "instances": 9, "metric_value": 0.3444, "depth": 13}
													if obj[3]>0:
														return 'False'
													elif obj[3]<=0:
														return 'False'
													else: return 'False'
												elif obj[11]>0:
													return 'True'
												else: return 'True'
											else: return 'False'
										else: return 'False'
									elif obj[7]>5:
										# {"feature": "Passanger", "instances": 145, "metric_value": 0.4519, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Direction_same", "instances": 86, "metric_value": 0.413, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Age", "instances": 51, "metric_value": 0.4696, "depth": 12}
												if obj[4]<=3:
													# {"feature": "Gender", "instances": 39, "metric_value": 0.4591, "depth": 13}
													if obj[3]>0:
														return 'False'
													elif obj[3]<=0:
														return 'False'
													else: return 'False'
												elif obj[4]>3:
													# {"feature": "Gender", "instances": 12, "metric_value": 0.5, "depth": 13}
													if obj[3]<=0:
														return 'True'
													elif obj[3]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[11]>0:
												# {"feature": "Gender", "instances": 35, "metric_value": 0.2882, "depth": 12}
												if obj[3]>0:
													# {"feature": "Age", "instances": 19, "metric_value": 0.386, "depth": 13}
													if obj[4]<=3:
														return 'False'
													elif obj[4]>3:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													# {"feature": "Age", "instances": 16, "metric_value": 0.1125, "depth": 13}
													if obj[4]>1:
														return 'False'
													elif obj[4]<=1:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[0]>1:
											# {"feature": "Direction_same", "instances": 59, "metric_value": 0.428, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Age", "instances": 52, "metric_value": 0.4507, "depth": 12}
												if obj[4]<=3:
													# {"feature": "Gender", "instances": 34, "metric_value": 0.4281, "depth": 13}
													if obj[3]>0:
														return 'False'
													elif obj[3]<=0:
														return 'False'
													else: return 'False'
												elif obj[4]>3:
													# {"feature": "Gender", "instances": 18, "metric_value": 0.4444, "depth": 13}
													if obj[3]<=0:
														return 'True'
													elif obj[3]>0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[11]>0:
												# {"feature": "Gender", "instances": 7, "metric_value": 0.1905, "depth": 12}
												if obj[3]<=0:
													return 'True'
												elif obj[3]>0:
													# {"feature": "Age", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[4]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'False'
									else: return 'False'
								elif obj[9]>3.0:
									# {"feature": "Gender", "instances": 26, "metric_value": 0.1122, "depth": 9}
									if obj[3]>0:
										# {"feature": "Occupation", "instances": 24, "metric_value": 0.0556, "depth": 10}
										if obj[7]>4:
											return 'False'
										elif obj[7]<=4:
											# {"feature": "Passanger", "instances": 3, "metric_value": 0.0, "depth": 11}
											if obj[0]>1:
												return 'False'
											elif obj[0]<=1:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[3]<=0:
										# {"feature": "Passanger", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Age", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[4]<=2:
												# {"feature": "Occupation", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[7]<=6:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[12]>2:
								# {"feature": "Passanger", "instances": 92, "metric_value": 0.1744, "depth": 8}
								if obj[0]<=1:
									# {"feature": "Occupation", "instances": 88, "metric_value": 0.1456, "depth": 9}
									if obj[7]<=12:
										# {"feature": "Age", "instances": 81, "metric_value": 0.113, "depth": 10}
										if obj[4]>1:
											# {"feature": "Gender", "instances": 59, "metric_value": 0.1502, "depth": 11}
											if obj[3]>0:
												# {"feature": "Coffeehouse", "instances": 44, "metric_value": 0.1981, "depth": 12}
												if obj[9]<=3.0:
													# {"feature": "Direction_same", "instances": 39, "metric_value": 0.2235, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[9]>3.0:
													return 'False'
												else: return 'False'
											elif obj[3]<=0:
												return 'False'
											else: return 'False'
										elif obj[4]<=1:
											return 'False'
										else: return 'False'
									elif obj[7]>12:
										# {"feature": "Age", "instances": 7, "metric_value": 0.381, "depth": 10}
										if obj[4]>0:
											# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.2667, "depth": 11}
											if obj[9]<=2.0:
												# {"feature": "Gender", "instances": 5, "metric_value": 0.32, "depth": 12}
												if obj[3]<=1:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[9]>2.0:
												return 'True'
											else: return 'True'
										elif obj[4]<=0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[0]>1:
									# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.0, "depth": 9}
									if obj[9]>-1.0:
										return 'True'
									elif obj[9]<=-1.0:
										return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'False'
						elif obj[1]>3:
							# {"feature": "Distance", "instances": 62, "metric_value": 0.1262, "depth": 7}
							if obj[12]>1:
								return 'False'
							elif obj[12]<=1:
								# {"feature": "Coffeehouse", "instances": 23, "metric_value": 0.2846, "depth": 8}
								if obj[9]>-1.0:
									# {"feature": "Occupation", "instances": 22, "metric_value": 0.2597, "depth": 9}
									if obj[7]>7:
										# {"feature": "Age", "instances": 14, "metric_value": 0.329, "depth": 10}
										if obj[4]<=2:
											# {"feature": "Passanger", "instances": 11, "metric_value": 0.2525, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Gender", "instances": 9, "metric_value": 0.1852, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.2778, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]>0:
													return 'False'
												else: return 'False'
											elif obj[0]>1:
												# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[3]<=1:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[4]>2:
											# {"feature": "Passanger", "instances": 3, "metric_value": 0.0, "depth": 11}
											if obj[0]<=1:
												return 'True'
											elif obj[0]>1:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[7]<=7:
										return 'False'
									else: return 'False'
								elif obj[9]<=-1.0:
									return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'False'
					elif obj[6]>4:
						# {"feature": "Passanger", "instances": 5, "metric_value": 0.2, "depth": 6}
						if obj[0]<=1:
							return 'True'
						elif obj[0]>1:
							# {"feature": "Time", "instances": 2, "metric_value": 0.0, "depth": 7}
							if obj[1]<=0:
								return 'True'
							elif obj[1]>0:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'True'
				elif obj[5]<=0:
					# {"feature": "Education", "instances": 434, "metric_value": 0.4372, "depth": 5}
					if obj[6]>0:
						# {"feature": "Occupation", "instances": 259, "metric_value": 0.385, "depth": 6}
						if obj[7]>2:
							# {"feature": "Age", "instances": 193, "metric_value": 0.4181, "depth": 7}
							if obj[4]>0:
								# {"feature": "Distance", "instances": 173, "metric_value": 0.401, "depth": 8}
								if obj[12]>1:
									# {"feature": "Time", "instances": 107, "metric_value": 0.3442, "depth": 9}
									if obj[1]<=2:
										# {"feature": "Coffeehouse", "instances": 77, "metric_value": 0.3944, "depth": 10}
										if obj[9]<=2.0:
											# {"feature": "Direction_same", "instances": 71, "metric_value": 0.4221, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Passanger", "instances": 69, "metric_value": 0.4303, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Gender", "instances": 65, "metric_value": 0.426, "depth": 13}
													if obj[3]<=0:
														return 'False'
													elif obj[3]>0:
														return 'False'
													else: return 'False'
												elif obj[0]>1:
													# {"feature": "Gender", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[3]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[11]>0:
												return 'False'
											else: return 'False'
										elif obj[9]>2.0:
											return 'False'
										else: return 'False'
									elif obj[1]>2:
										# {"feature": "Passanger", "instances": 30, "metric_value": 0.1625, "depth": 10}
										if obj[0]>1:
											# {"feature": "Gender", "instances": 16, "metric_value": 0.2792, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Coffeehouse", "instances": 10, "metric_value": 0.15, "depth": 12}
												if obj[9]<=0.0:
													return 'False'
												elif obj[9]>0.0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[3]>0:
												# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.0, "depth": 12}
												if obj[9]>0.0:
													return 'False'
												elif obj[9]<=0.0:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[0]<=1:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[12]<=1:
									# {"feature": "Coffeehouse", "instances": 66, "metric_value": 0.4616, "depth": 9}
									if obj[9]>-1.0:
										# {"feature": "Passanger", "instances": 64, "metric_value": 0.468, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Time", "instances": 57, "metric_value": 0.462, "depth": 11}
											if obj[1]>0:
												# {"feature": "Gender", "instances": 33, "metric_value": 0.4311, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 19, "metric_value": 0.3801, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 14, "metric_value": 0.4898, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[1]<=0:
												# {"feature": "Gender", "instances": 24, "metric_value": 0.4044, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 13, "metric_value": 0.355, "depth": 13}
													if obj[11]<=1:
														return 'False'
													else: return 'False'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 11, "metric_value": 0.4628, "depth": 13}
													if obj[11]<=1:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[0]>1:
											# {"feature": "Gender", "instances": 7, "metric_value": 0.4048, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Time", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[1]<=4:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Time", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[1]<=4:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[9]<=-1.0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[4]<=0:
								# {"feature": "Coffeehouse", "instances": 20, "metric_value": 0.3733, "depth": 8}
								if obj[9]<=1.0:
									# {"feature": "Time", "instances": 15, "metric_value": 0.4394, "depth": 9}
									if obj[1]>0:
										# {"feature": "Direction_same", "instances": 11, "metric_value": 0.4364, "depth": 10}
										if obj[11]<=0:
											# {"feature": "Distance", "instances": 10, "metric_value": 0.4444, "depth": 11}
											if obj[12]<=2:
												# {"feature": "Passanger", "instances": 9, "metric_value": 0.4815, "depth": 12}
												if obj[0]>0:
													# {"feature": "Gender", "instances": 6, "metric_value": 0.5, "depth": 13}
													if obj[3]<=0:
														return 'True'
													else: return 'True'
												elif obj[0]<=0:
													# {"feature": "Gender", "instances": 3, "metric_value": 0.3333, "depth": 13}
													if obj[3]>0:
														return 'False'
													elif obj[3]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[12]>2:
												return 'False'
											else: return 'False'
										elif obj[11]>0:
											return 'False'
										else: return 'False'
									elif obj[1]<=0:
										# {"feature": "Direction_same", "instances": 4, "metric_value": 0.3333, "depth": 10}
										if obj[11]<=0:
											# {"feature": "Passanger", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Distance", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[12]<=3:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[11]>0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[9]>1.0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[7]<=2:
							# {"feature": "Coffeehouse", "instances": 66, "metric_value": 0.2165, "depth": 7}
							if obj[9]>0.0:
								# {"feature": "Age", "instances": 38, "metric_value": 0.0789, "depth": 8}
								if obj[4]<=6:
									return 'False'
								elif obj[4]>6:
									# {"feature": "Distance", "instances": 8, "metric_value": 0.25, "depth": 9}
									if obj[12]>1:
										# {"feature": "Passanger", "instances": 4, "metric_value": 0.3333, "depth": 10}
										if obj[0]>0:
											# {"feature": "Time", "instances": 3, "metric_value": 0.3333, "depth": 11}
											if obj[1]<=1:
												# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[3]<=1:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[1]>1:
												return 'True'
											else: return 'True'
										elif obj[0]<=0:
											return 'False'
										else: return 'False'
									elif obj[12]<=1:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[9]<=0.0:
								# {"feature": "Time", "instances": 28, "metric_value": 0.3436, "depth": 8}
								if obj[1]>2:
									# {"feature": "Passanger", "instances": 15, "metric_value": 0.1333, "depth": 9}
									if obj[0]>0:
										return 'False'
									elif obj[0]<=0:
										# {"feature": "Age", "instances": 4, "metric_value": 0.3333, "depth": 10}
										if obj[4]<=5:
											# {"feature": "Gender", "instances": 3, "metric_value": 0.3333, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[12]<=1:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]>0:
												return 'True'
											else: return 'True'
										elif obj[4]>5:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[1]<=2:
									# {"feature": "Direction_same", "instances": 13, "metric_value": 0.3846, "depth": 9}
									if obj[11]<=0:
										# {"feature": "Age", "instances": 10, "metric_value": 0.375, "depth": 10}
										if obj[4]<=5:
											# {"feature": "Passanger", "instances": 8, "metric_value": 0.4286, "depth": 11}
											if obj[0]>0:
												# {"feature": "Distance", "instances": 7, "metric_value": 0.4286, "depth": 12}
												if obj[12]<=2:
													# {"feature": "Gender", "instances": 6, "metric_value": 0.5, "depth": 13}
													if obj[3]>0:
														return 'True'
													elif obj[3]<=0:
														return 'False'
													else: return 'False'
												elif obj[12]>2:
													return 'False'
												else: return 'False'
											elif obj[0]<=0:
												return 'False'
											else: return 'False'
										elif obj[4]>5:
											return 'True'
										else: return 'True'
									elif obj[11]>0:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[6]<=0:
						# {"feature": "Distance", "instances": 175, "metric_value": 0.4764, "depth": 6}
						if obj[12]<=2:
							# {"feature": "Occupation", "instances": 140, "metric_value": 0.4782, "depth": 7}
							if obj[7]>4:
								# {"feature": "Coffeehouse", "instances": 110, "metric_value": 0.4791, "depth": 8}
								if obj[9]>-1.0:
									# {"feature": "Gender", "instances": 106, "metric_value": 0.4796, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Passanger", "instances": 63, "metric_value": 0.4695, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Age", "instances": 50, "metric_value": 0.479, "depth": 11}
											if obj[4]>3:
												# {"feature": "Time", "instances": 42, "metric_value": 0.4954, "depth": 12}
												if obj[1]<=2:
													# {"feature": "Direction_same", "instances": 29, "metric_value": 0.4932, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												elif obj[1]>2:
													# {"feature": "Direction_same", "instances": 13, "metric_value": 0.4196, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[4]<=3:
												# {"feature": "Time", "instances": 8, "metric_value": 0.1667, "depth": 12}
												if obj[1]<=1:
													return 'True'
												elif obj[1]>1:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[0]>1:
											# {"feature": "Age", "instances": 13, "metric_value": 0.3077, "depth": 11}
											if obj[4]>4:
												# {"feature": "Time", "instances": 9, "metric_value": 0.3333, "depth": 12}
												if obj[1]>2:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[1]<=2:
													return 'False'
												else: return 'False'
											elif obj[4]<=4:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[3]>0:
										# {"feature": "Age", "instances": 43, "metric_value": 0.4306, "depth": 10}
										if obj[4]<=4:
											# {"feature": "Passanger", "instances": 28, "metric_value": 0.4354, "depth": 11}
											if obj[0]>0:
												# {"feature": "Time", "instances": 21, "metric_value": 0.4626, "depth": 12}
												if obj[1]<=3:
													# {"feature": "Direction_same", "instances": 14, "metric_value": 0.4889, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[1]>3:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4082, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[0]<=0:
												# {"feature": "Time", "instances": 7, "metric_value": 0.2143, "depth": 12}
												if obj[1]>2:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[1]<=2:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[4]>4:
											# {"feature": "Time", "instances": 15, "metric_value": 0.2286, "depth": 11}
											if obj[1]>1:
												return 'True'
											elif obj[1]<=1:
												# {"feature": "Passanger", "instances": 7, "metric_value": 0.381, "depth": 12}
												if obj[0]>0:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4167, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												elif obj[0]<=0:
													return 'False'
												else: return 'False'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[9]<=-1.0:
									return 'True'
								else: return 'True'
							elif obj[7]<=4:
								# {"feature": "Coffeehouse", "instances": 30, "metric_value": 0.175, "depth": 8}
								if obj[9]<=2.0:
									# {"feature": "Age", "instances": 24, "metric_value": 0.1522, "depth": 9}
									if obj[4]>0:
										# {"feature": "Passanger", "instances": 23, "metric_value": 0.087, "depth": 10}
										if obj[0]<=1:
											return 'False'
										elif obj[0]>1:
											# {"feature": "Time", "instances": 4, "metric_value": 0.0, "depth": 11}
											if obj[1]>3:
												return 'False'
											elif obj[1]<=3:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[4]<=0:
										return 'True'
									else: return 'True'
								elif obj[9]>2.0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[12]>2:
							# {"feature": "Occupation", "instances": 35, "metric_value": 0.2786, "depth": 7}
							if obj[7]>0:
								# {"feature": "Age", "instances": 32, "metric_value": 0.2772, "depth": 8}
								if obj[4]>2:
									# {"feature": "Time", "instances": 23, "metric_value": 0.3616, "depth": 9}
									if obj[1]>0:
										# {"feature": "Gender", "instances": 19, "metric_value": 0.3185, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.2462, "depth": 11}
											if obj[9]<=2.0:
												# {"feature": "Passanger", "instances": 10, "metric_value": 0.32, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Direction_same", "instances": 10, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[9]>2.0:
												return 'False'
											else: return 'False'
										elif obj[3]>0:
											# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.2667, "depth": 11}
											if obj[9]<=2.0:
												# {"feature": "Passanger", "instances": 5, "metric_value": 0.32, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[9]>2.0:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[1]<=0:
										# {"feature": "Gender", "instances": 4, "metric_value": 0.3333, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.3333, "depth": 11}
											if obj[9]<=0.0:
												# {"feature": "Passanger", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[9]>0.0:
												return 'True'
											else: return 'True'
										elif obj[3]>0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[4]<=2:
									return 'False'
								else: return 'False'
							elif obj[7]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[10]>2.0:
				# {"feature": "Age", "instances": 48, "metric_value": 0.3792, "depth": 4}
				if obj[4]>0:
					# {"feature": "Gender", "instances": 40, "metric_value": 0.4147, "depth": 5}
					if obj[3]>0:
						# {"feature": "Occupation", "instances": 25, "metric_value": 0.2743, "depth": 6}
						if obj[7]<=4:
							# {"feature": "Passanger", "instances": 14, "metric_value": 0.4286, "depth": 7}
							if obj[0]<=2:
								# {"feature": "Time", "instances": 12, "metric_value": 0.4375, "depth": 8}
								if obj[1]<=2:
									# {"feature": "Direction_same", "instances": 8, "metric_value": 0.4375, "depth": 9}
									if obj[11]>0:
										# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.25, "depth": 10}
										if obj[9]>2.0:
											return 'True'
										elif obj[9]<=2.0:
											# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[5]<=1:
												# {"feature": "Education", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[6]<=0:
													# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[12]<=2:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[11]<=0:
										# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.3333, "depth": 10}
										if obj[9]<=2.0:
											# {"feature": "Distance", "instances": 3, "metric_value": 0.3333, "depth": 11}
											if obj[12]>1:
												# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[5]<=1:
													# {"feature": "Education", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[6]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[12]<=1:
												return 'True'
											else: return 'True'
										elif obj[9]>2.0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[1]>2:
									# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.25, "depth": 9}
									if obj[9]<=2.0:
										# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[5]<=1:
											# {"feature": "Education", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[6]<=0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[12]<=2:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[9]>2.0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[0]>2:
								return 'True'
							else: return 'True'
						elif obj[7]>4:
							return 'True'
						else: return 'True'
					elif obj[3]<=0:
						# {"feature": "Time", "instances": 15, "metric_value": 0.4267, "depth": 6}
						if obj[1]>1:
							# {"feature": "Occupation", "instances": 10, "metric_value": 0.419, "depth": 7}
							if obj[7]<=7:
								# {"feature": "Distance", "instances": 7, "metric_value": 0.3429, "depth": 8}
								if obj[12]>1:
									# {"feature": "Passanger", "instances": 5, "metric_value": 0.4667, "depth": 9}
									if obj[0]>1:
										# {"feature": "Children", "instances": 3, "metric_value": 0.3333, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Education", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[6]<=4:
												# {"feature": "Coffeehouse", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[9]<=1.0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[5]>0:
											return 'True'
										else: return 'True'
									elif obj[0]<=1:
										# {"feature": "Children", "instances": 2, "metric_value": 0.0, "depth": 10}
										if obj[5]<=0:
											return 'True'
										elif obj[5]>0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[12]<=1:
									return 'True'
								else: return 'True'
							elif obj[7]>7:
								# {"feature": "Direction_same", "instances": 3, "metric_value": 0.0, "depth": 8}
								if obj[11]<=0:
									return 'False'
								elif obj[11]>0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[1]<=1:
							# {"feature": "Children", "instances": 5, "metric_value": 0.2667, "depth": 7}
							if obj[5]<=0:
								# {"feature": "Direction_same", "instances": 3, "metric_value": 0.3333, "depth": 8}
								if obj[11]<=0:
									# {"feature": "Passanger", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Education", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[6]<=4:
											# {"feature": "Occupation", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[7]<=7:
												# {"feature": "Coffeehouse", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[9]<=1.0:
													# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[12]<=3:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[11]>0:
									return 'False'
								else: return 'False'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[4]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	else: return 'False'
