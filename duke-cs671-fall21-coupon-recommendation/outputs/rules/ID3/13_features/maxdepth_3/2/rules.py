def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Coupon", "instances": 8147, "metric_value": 0.4734, "depth": 1}
	if obj[2]>1:
		# {"feature": "Coffeehouse", "instances": 5886, "metric_value": 0.4595, "depth": 2}
		if obj[9]<=1.0:
			# {"feature": "Distance", "instances": 3041, "metric_value": 0.4864, "depth": 3}
			if obj[12]<=2:
				# {"feature": "Passanger", "instances": 2734, "metric_value": 0.4834, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Restaurant20to50", "instances": 1643, "metric_value": 0.4939, "depth": 5}
					if obj[10]<=2.0:
						# {"feature": "Gender", "instances": 1593, "metric_value": 0.4963, "depth": 6}
						if obj[3]<=0:
							# {"feature": "Education", "instances": 803, "metric_value": 0.4917, "depth": 7}
							if obj[6]>1:
								# {"feature": "Age", "instances": 442, "metric_value": 0.4914, "depth": 8}
								if obj[4]>0:
									# {"feature": "Occupation", "instances": 364, "metric_value": 0.4929, "depth": 9}
									if obj[7]>1:
										# {"feature": "Time", "instances": 336, "metric_value": 0.4967, "depth": 10}
										if obj[1]<=3:
											# {"feature": "Bar", "instances": 277, "metric_value": 0.4939, "depth": 11}
											if obj[8]>-1.0:
												# {"feature": "Direction_same", "instances": 274, "metric_value": 0.4992, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Children", "instances": 149, "metric_value": 0.4981, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'False'
													else: return 'False'
												elif obj[11]>0:
													# {"feature": "Children", "instances": 125, "metric_value": 0.4937, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[8]<=-1.0:
												return 'False'
											else: return 'False'
										elif obj[1]>3:
											# {"feature": "Bar", "instances": 59, "metric_value": 0.4754, "depth": 11}
											if obj[8]>-1.0:
												# {"feature": "Children", "instances": 56, "metric_value": 0.4697, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 51, "metric_value": 0.4844, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[8]<=-1.0:
												# {"feature": "Children", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[5]<=1:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[7]<=1:
										# {"feature": "Bar", "instances": 28, "metric_value": 0.381, "depth": 10}
										if obj[8]>-1.0:
											# {"feature": "Time", "instances": 24, "metric_value": 0.4048, "depth": 11}
											if obj[1]<=1:
												# {"feature": "Direction_same", "instances": 14, "metric_value": 0.2984, "depth": 12}
												if obj[11]>0:
													# {"feature": "Children", "instances": 9, "metric_value": 0.1975, "depth": 13}
													if obj[5]<=0:
														return 'True'
													else: return 'True'
												elif obj[11]<=0:
													# {"feature": "Children", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[5]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[1]>1:
												# {"feature": "Direction_same", "instances": 10, "metric_value": 0.375, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Children", "instances": 8, "metric_value": 0.4688, "depth": 13}
													if obj[5]<=0:
														return 'True'
													else: return 'True'
												elif obj[11]>0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[8]<=-1.0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[4]<=0:
									# {"feature": "Bar", "instances": 78, "metric_value": 0.3921, "depth": 9}
									if obj[8]<=1.0:
										# {"feature": "Occupation", "instances": 68, "metric_value": 0.3623, "depth": 10}
										if obj[7]<=8:
											# {"feature": "Children", "instances": 45, "metric_value": 0.2723, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Time", "instances": 29, "metric_value": 0.1182, "depth": 12}
												if obj[1]>0:
													return 'True'
												elif obj[1]<=0:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4857, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[5]>0:
												# {"feature": "Direction_same", "instances": 16, "metric_value": 0.4062, "depth": 12}
												if obj[11]>0:
													# {"feature": "Time", "instances": 12, "metric_value": 0.3333, "depth": 13}
													if obj[1]>0:
														return 'True'
													elif obj[1]<=0:
														return 'True'
													else: return 'True'
												elif obj[11]<=0:
													# {"feature": "Time", "instances": 4, "metric_value": 0.3333, "depth": 13}
													if obj[1]<=1:
														return 'False'
													elif obj[1]>1:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[7]>8:
											# {"feature": "Time", "instances": 23, "metric_value": 0.4783, "depth": 11}
											if obj[1]<=3:
												# {"feature": "Direction_same", "instances": 22, "metric_value": 0.4833, "depth": 12}
												if obj[11]>0:
													# {"feature": "Children", "instances": 12, "metric_value": 0.4815, "depth": 13}
													if obj[5]>0:
														return 'True'
													elif obj[5]<=0:
														return 'True'
													else: return 'True'
												elif obj[11]<=0:
													# {"feature": "Children", "instances": 10, "metric_value": 0.4762, "depth": 13}
													if obj[5]>0:
														return 'False'
													elif obj[5]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[1]>3:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[8]>1.0:
										# {"feature": "Time", "instances": 10, "metric_value": 0.1778, "depth": 10}
										if obj[1]<=3:
											# {"feature": "Direction_same", "instances": 9, "metric_value": 0.1667, "depth": 11}
											if obj[11]>0:
												return 'False'
											elif obj[11]<=0:
												# {"feature": "Children", "instances": 4, "metric_value": 0.25, "depth": 12}
												if obj[5]>0:
													return 'False'
												elif obj[5]<=0:
													# {"feature": "Occupation", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[7]<=24:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[1]>3:
											return 'True'
										else: return 'True'
									else: return 'False'
								else: return 'True'
							elif obj[6]<=1:
								# {"feature": "Occupation", "instances": 361, "metric_value": 0.4732, "depth": 8}
								if obj[7]<=18:
									# {"feature": "Age", "instances": 327, "metric_value": 0.4854, "depth": 9}
									if obj[4]<=4:
										# {"feature": "Bar", "instances": 249, "metric_value": 0.491, "depth": 10}
										if obj[8]>0.0:
											# {"feature": "Time", "instances": 164, "metric_value": 0.4823, "depth": 11}
											if obj[1]<=2:
												# {"feature": "Children", "instances": 118, "metric_value": 0.4738, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 96, "metric_value": 0.4642, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 22, "metric_value": 0.4817, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												else: return 'True'
											elif obj[1]>2:
												# {"feature": "Children", "instances": 46, "metric_value": 0.4888, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 37, "metric_value": 0.4995, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4167, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[8]<=0.0:
											# {"feature": "Direction_same", "instances": 85, "metric_value": 0.4799, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Time", "instances": 63, "metric_value": 0.4736, "depth": 12}
												if obj[1]<=3:
													# {"feature": "Children", "instances": 44, "metric_value": 0.4481, "depth": 13}
													if obj[5]<=0:
														return 'False'
													elif obj[5]>0:
														return 'False'
													else: return 'False'
												elif obj[1]>3:
													# {"feature": "Children", "instances": 19, "metric_value": 0.4872, "depth": 13}
													if obj[5]<=0:
														return 'False'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												else: return 'False'
											elif obj[11]>0:
												# {"feature": "Time", "instances": 22, "metric_value": 0.4578, "depth": 12}
												if obj[1]<=1:
													# {"feature": "Children", "instances": 17, "metric_value": 0.4373, "depth": 13}
													if obj[5]<=0:
														return 'False'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												elif obj[1]>1:
													# {"feature": "Children", "instances": 5, "metric_value": 0.2, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[4]>4:
										# {"feature": "Time", "instances": 78, "metric_value": 0.4097, "depth": 10}
										if obj[1]<=1:
											# {"feature": "Bar", "instances": 48, "metric_value": 0.4822, "depth": 11}
											if obj[8]<=1.0:
												# {"feature": "Direction_same", "instances": 38, "metric_value": 0.4943, "depth": 12}
												if obj[11]>0:
													# {"feature": "Children", "instances": 25, "metric_value": 0.4905, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'False'
													else: return 'False'
												elif obj[11]<=0:
													# {"feature": "Children", "instances": 13, "metric_value": 0.4957, "depth": 13}
													if obj[5]<=0:
														return 'False'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												else: return 'False'
											elif obj[8]>1.0:
												# {"feature": "Direction_same", "instances": 10, "metric_value": 0.3429, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Children", "instances": 7, "metric_value": 0.4762, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												elif obj[11]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[1]>1:
											# {"feature": "Bar", "instances": 30, "metric_value": 0.2716, "depth": 11}
											if obj[8]<=1.0:
												# {"feature": "Children", "instances": 27, "metric_value": 0.2982, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 19, "metric_value": 0.2647, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.3571, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[8]>1.0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[7]>18:
									# {"feature": "Bar", "instances": 34, "metric_value": 0.2609, "depth": 9}
									if obj[8]>0.0:
										# {"feature": "Children", "instances": 23, "metric_value": 0.3559, "depth": 10}
										if obj[5]>0:
											# {"feature": "Time", "instances": 13, "metric_value": 0.2198, "depth": 11}
											if obj[1]<=1:
												# {"feature": "Age", "instances": 7, "metric_value": 0.4048, "depth": 12}
												if obj[4]>0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.3333, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[4]<=0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.3333, "depth": 13}
													if obj[11]>0:
														return 'True'
													elif obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[1]>1:
												return 'True'
											else: return 'True'
										elif obj[5]<=0:
											# {"feature": "Direction_same", "instances": 10, "metric_value": 0.4, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Time", "instances": 5, "metric_value": 0.4, "depth": 12}
												if obj[1]<=3:
													# {"feature": "Age", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[4]<=1:
														return 'False'
													elif obj[4]>1:
														return 'False'
													else: return 'False'
												elif obj[1]>3:
													return 'False'
												else: return 'False'
											elif obj[11]>0:
												# {"feature": "Time", "instances": 5, "metric_value": 0.0, "depth": 12}
												if obj[1]<=1:
													return 'True'
												elif obj[1]>1:
													return 'False'
												else: return 'False'
											else: return 'True'
										else: return 'True'
									elif obj[8]<=0.0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[3]>0:
							# {"feature": "Bar", "instances": 790, "metric_value": 0.4942, "depth": 7}
							if obj[8]>-1.0:
								# {"feature": "Occupation", "instances": 782, "metric_value": 0.4958, "depth": 8}
								if obj[7]<=19:
									# {"feature": "Time", "instances": 723, "metric_value": 0.4956, "depth": 9}
									if obj[1]>0:
										# {"feature": "Age", "instances": 511, "metric_value": 0.4893, "depth": 10}
										if obj[4]<=6:
											# {"feature": "Education", "instances": 491, "metric_value": 0.4932, "depth": 11}
											if obj[6]>1:
												# {"feature": "Children", "instances": 249, "metric_value": 0.4873, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 161, "metric_value": 0.4938, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 88, "metric_value": 0.4697, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[6]<=1:
												# {"feature": "Direction_same", "instances": 242, "metric_value": 0.4831, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Children", "instances": 148, "metric_value": 0.4729, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												elif obj[11]>0:
													# {"feature": "Children", "instances": 94, "metric_value": 0.4972, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[4]>6:
											# {"feature": "Education", "instances": 20, "metric_value": 0.2933, "depth": 11}
											if obj[6]<=2:
												# {"feature": "Direction_same", "instances": 15, "metric_value": 0.3852, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Children", "instances": 9, "metric_value": 0.2963, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												elif obj[11]>0:
													# {"feature": "Children", "instances": 6, "metric_value": 0.4167, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'False'
													else: return 'False'
												else: return 'True'
											elif obj[6]>2:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[1]<=0:
										# {"feature": "Direction_same", "instances": 212, "metric_value": 0.4927, "depth": 10}
										if obj[11]<=0:
											# {"feature": "Children", "instances": 111, "metric_value": 0.4723, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Education", "instances": 64, "metric_value": 0.4759, "depth": 12}
												if obj[6]>0:
													# {"feature": "Age", "instances": 35, "metric_value": 0.4484, "depth": 13}
													if obj[4]>0:
														return 'False'
													elif obj[4]<=0:
														return 'True'
													else: return 'True'
												elif obj[6]<=0:
													# {"feature": "Age", "instances": 29, "metric_value": 0.4121, "depth": 13}
													if obj[4]>0:
														return 'True'
													elif obj[4]<=0:
														return 'False'
													else: return 'False'
												else: return 'True'
											elif obj[5]>0:
												# {"feature": "Age", "instances": 47, "metric_value": 0.4186, "depth": 12}
												if obj[4]>1:
													# {"feature": "Education", "instances": 35, "metric_value": 0.4506, "depth": 13}
													if obj[6]<=3:
														return 'False'
													elif obj[6]>3:
														return 'True'
													else: return 'True'
												elif obj[4]<=1:
													# {"feature": "Education", "instances": 12, "metric_value": 0.2381, "depth": 13}
													if obj[6]>0:
														return 'False'
													elif obj[6]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[11]>0:
											# {"feature": "Education", "instances": 101, "metric_value": 0.474, "depth": 11}
											if obj[6]>0:
												# {"feature": "Children", "instances": 63, "metric_value": 0.4463, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Age", "instances": 41, "metric_value": 0.4753, "depth": 13}
													if obj[4]>0:
														return 'True'
													elif obj[4]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Age", "instances": 22, "metric_value": 0.2944, "depth": 13}
													if obj[4]<=6:
														return 'True'
													elif obj[4]>6:
														return 'False'
													else: return 'False'
												else: return 'True'
											elif obj[6]<=0:
												# {"feature": "Age", "instances": 38, "metric_value": 0.4528, "depth": 12}
												if obj[4]<=3:
													# {"feature": "Children", "instances": 23, "metric_value": 0.4101, "depth": 13}
													if obj[5]<=0:
														return 'False'
													elif obj[5]>0:
														return 'False'
													else: return 'False'
												elif obj[4]>3:
													# {"feature": "Children", "instances": 15, "metric_value": 0.4778, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'False'
													else: return 'False'
												else: return 'True'
											else: return 'False'
										else: return 'True'
									else: return 'False'
								elif obj[7]>19:
									# {"feature": "Education", "instances": 59, "metric_value": 0.4348, "depth": 9}
									if obj[6]<=2:
										# {"feature": "Time", "instances": 45, "metric_value": 0.4567, "depth": 10}
										if obj[1]<=2:
											# {"feature": "Age", "instances": 32, "metric_value": 0.4674, "depth": 11}
											if obj[4]<=3:
												# {"feature": "Children", "instances": 23, "metric_value": 0.4224, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 16, "metric_value": 0.4667, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[5]<=0:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.2381, "depth": 13}
													if obj[11]>0:
														return 'True'
													elif obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[4]>3:
												# {"feature": "Children", "instances": 9, "metric_value": 0.4333, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.3, "depth": 13}
													if obj[11]>0:
														return 'False'
													elif obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.25, "depth": 13}
													if obj[11]>0:
														return 'False'
													elif obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[1]>2:
											# {"feature": "Direction_same", "instances": 13, "metric_value": 0.3192, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Age", "instances": 8, "metric_value": 0.0, "depth": 12}
												if obj[4]>1:
													return 'False'
												elif obj[4]<=1:
													return 'True'
												else: return 'True'
											elif obj[11]>0:
												# {"feature": "Age", "instances": 5, "metric_value": 0.0, "depth": 12}
												if obj[4]<=1:
													return 'False'
												elif obj[4]>1:
													return 'True'
												else: return 'True'
											else: return 'False'
										else: return 'False'
									elif obj[6]>2:
										# {"feature": "Age", "instances": 14, "metric_value": 0.1714, "depth": 10}
										if obj[4]<=1:
											return 'False'
										elif obj[4]>1:
											# {"feature": "Time", "instances": 5, "metric_value": 0.3, "depth": 11}
											if obj[1]>0:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.25, "depth": 12}
												if obj[11]>0:
													return 'False'
												elif obj[11]<=0:
													# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[5]<=1:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[1]<=0:
												return 'True'
											else: return 'True'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[8]<=-1.0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[10]>2.0:
						# {"feature": "Time", "instances": 50, "metric_value": 0.3467, "depth": 6}
						if obj[1]>0:
							# {"feature": "Occupation", "instances": 39, "metric_value": 0.404, "depth": 7}
							if obj[7]<=9:
								# {"feature": "Age", "instances": 33, "metric_value": 0.3827, "depth": 8}
								if obj[4]>0:
									# {"feature": "Direction_same", "instances": 25, "metric_value": 0.416, "depth": 9}
									if obj[11]<=0:
										# {"feature": "Children", "instances": 15, "metric_value": 0.4727, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Gender", "instances": 11, "metric_value": 0.4606, "depth": 11}
											if obj[3]>0:
												# {"feature": "Education", "instances": 6, "metric_value": 0.4444, "depth": 12}
												if obj[6]>1:
													# {"feature": "Bar", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[8]<=2.0:
														return 'True'
													else: return 'True'
												elif obj[6]<=1:
													# {"feature": "Bar", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[8]<=2.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Education", "instances": 5, "metric_value": 0.48, "depth": 12}
												if obj[6]<=4:
													# {"feature": "Bar", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[8]<=0.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[5]>0:
											# {"feature": "Gender", "instances": 4, "metric_value": 0.5, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Education", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[6]<=4:
													# {"feature": "Bar", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[8]<=0.0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[11]>0:
										# {"feature": "Gender", "instances": 10, "metric_value": 0.1778, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Children", "instances": 9, "metric_value": 0.1481, "depth": 11}
											if obj[5]<=0:
												return 'True'
											elif obj[5]>0:
												# {"feature": "Education", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[6]<=4:
													# {"feature": "Bar", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[8]<=0.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]>0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[4]<=0:
									# {"feature": "Direction_same", "instances": 8, "metric_value": 0.1667, "depth": 9}
									if obj[11]<=0:
										return 'True'
									elif obj[11]>0:
										# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[3]<=1:
											# {"feature": "Children", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[5]<=1:
												# {"feature": "Education", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[6]<=0:
													# {"feature": "Bar", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[8]<=1.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[7]>9:
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
					if obj[6]>1:
						# {"feature": "Time", "instances": 569, "metric_value": 0.4738, "depth": 6}
						if obj[1]>0:
							# {"feature": "Restaurant20to50", "instances": 439, "metric_value": 0.486, "depth": 7}
							if obj[10]>0.0:
								# {"feature": "Age", "instances": 331, "metric_value": 0.493, "depth": 8}
								if obj[4]<=5:
									# {"feature": "Occupation", "instances": 271, "metric_value": 0.4881, "depth": 9}
									if obj[7]>1:
										# {"feature": "Bar", "instances": 246, "metric_value": 0.4952, "depth": 10}
										if obj[8]<=1.0:
											# {"feature": "Children", "instances": 170, "metric_value": 0.491, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Gender", "instances": 99, "metric_value": 0.4707, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 56, "metric_value": 0.4483, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 43, "metric_value": 0.4997, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[5]>0:
												# {"feature": "Gender", "instances": 71, "metric_value": 0.488, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 43, "metric_value": 0.4867, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 28, "metric_value": 0.4898, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[8]>1.0:
											# {"feature": "Children", "instances": 76, "metric_value": 0.4996, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Gender", "instances": 49, "metric_value": 0.4994, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 32, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 17, "metric_value": 0.4983, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[5]>0:
												# {"feature": "Gender", "instances": 27, "metric_value": 0.4938, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 18, "metric_value": 0.4938, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4938, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'True'
										else: return 'True'
									elif obj[7]<=1:
										# {"feature": "Bar", "instances": 25, "metric_value": 0.3947, "depth": 10}
										if obj[8]>0.0:
											# {"feature": "Gender", "instances": 15, "metric_value": 0.4405, "depth": 11}
											if obj[3]>0:
												# {"feature": "Children", "instances": 8, "metric_value": 0.4688, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.4688, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Children", "instances": 7, "metric_value": 0.4082, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4082, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[8]<=0.0:
											# {"feature": "Gender", "instances": 10, "metric_value": 0.3, "depth": 11}
											if obj[3]>0:
												# {"feature": "Children", "instances": 8, "metric_value": 0.375, "depth": 12}
												if obj[5]<=1:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[4]>5:
									# {"feature": "Occupation", "instances": 60, "metric_value": 0.4415, "depth": 9}
									if obj[7]<=19:
										# {"feature": "Gender", "instances": 53, "metric_value": 0.4913, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Bar", "instances": 30, "metric_value": 0.4833, "depth": 11}
											if obj[8]>0.0:
												# {"feature": "Children", "instances": 16, "metric_value": 0.4583, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 12, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[5]<=0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[8]<=0.0:
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
											else: return 'True'
										elif obj[3]>0:
											# {"feature": "Children", "instances": 23, "metric_value": 0.4908, "depth": 11}
											if obj[5]>0:
												# {"feature": "Bar", "instances": 18, "metric_value": 0.4907, "depth": 12}
												if obj[8]>0.0:
													# {"feature": "Direction_same", "instances": 12, "metric_value": 0.4861, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[8]<=0.0:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[5]<=0:
												# {"feature": "Bar", "instances": 5, "metric_value": 0.4, "depth": 12}
												if obj[8]>0.0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[8]<=0.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[7]>19:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[10]<=0.0:
								# {"feature": "Bar", "instances": 108, "metric_value": 0.4265, "depth": 8}
								if obj[8]<=1.0:
									# {"feature": "Occupation", "instances": 98, "metric_value": 0.4579, "depth": 9}
									if obj[7]<=20:
										# {"feature": "Age", "instances": 94, "metric_value": 0.462, "depth": 10}
										if obj[4]<=2:
											# {"feature": "Gender", "instances": 56, "metric_value": 0.426, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Children", "instances": 28, "metric_value": 0.477, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 18, "metric_value": 0.4753, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 10, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Children", "instances": 28, "metric_value": 0.3724, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 14, "metric_value": 0.4082, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 14, "metric_value": 0.3367, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[4]>2:
											# {"feature": "Gender", "instances": 38, "metric_value": 0.4985, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Children", "instances": 25, "metric_value": 0.4988, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 17, "metric_value": 0.4983, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[3]>0:
												# {"feature": "Children", "instances": 13, "metric_value": 0.4965, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 11, "metric_value": 0.4959, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[7]>20:
										return 'True'
									else: return 'True'
								elif obj[8]>1.0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[1]<=0:
							# {"feature": "Occupation", "instances": 130, "metric_value": 0.3967, "depth": 7}
							if obj[7]<=6:
								# {"feature": "Age", "instances": 65, "metric_value": 0.3082, "depth": 8}
								if obj[4]<=6:
									# {"feature": "Restaurant20to50", "instances": 61, "metric_value": 0.2842, "depth": 9}
									if obj[10]>0.0:
										# {"feature": "Bar", "instances": 44, "metric_value": 0.3463, "depth": 10}
										if obj[8]<=2.0:
											# {"feature": "Children", "instances": 42, "metric_value": 0.3576, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Gender", "instances": 25, "metric_value": 0.4024, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 17, "metric_value": 0.4152, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[5]>0:
												# {"feature": "Gender", "instances": 17, "metric_value": 0.2353, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[8]>2.0:
											return 'True'
										else: return 'True'
									elif obj[10]<=0.0:
										# {"feature": "Bar", "instances": 17, "metric_value": 0.1029, "depth": 10}
										if obj[8]<=0.0:
											return 'True'
										elif obj[8]>0.0:
											# {"feature": "Gender", "instances": 8, "metric_value": 0.1875, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Children", "instances": 4, "metric_value": 0.25, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[4]>6:
									# {"feature": "Children", "instances": 4, "metric_value": 0.3333, "depth": 9}
									if obj[5]<=0:
										# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.3333, "depth": 10}
										if obj[10]<=0.0:
											# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[3]<=1:
												# {"feature": "Bar", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[8]<=0.0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[10]>0.0:
											return 'False'
										else: return 'False'
									elif obj[5]>0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[7]>6:
								# {"feature": "Age", "instances": 65, "metric_value": 0.4572, "depth": 8}
								if obj[4]<=6:
									# {"feature": "Gender", "instances": 59, "metric_value": 0.4525, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Bar", "instances": 32, "metric_value": 0.4718, "depth": 10}
										if obj[8]<=3.0:
											# {"feature": "Restaurant20to50", "instances": 31, "metric_value": 0.4753, "depth": 11}
											if obj[10]<=2.0:
												# {"feature": "Children", "instances": 30, "metric_value": 0.4906, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 19, "metric_value": 0.4875, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 11, "metric_value": 0.4959, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[10]>2.0:
												return 'True'
											else: return 'True'
										elif obj[8]>3.0:
											return 'True'
										else: return 'True'
									elif obj[3]>0:
										# {"feature": "Restaurant20to50", "instances": 27, "metric_value": 0.3771, "depth": 10}
										if obj[10]>0.0:
											# {"feature": "Bar", "instances": 22, "metric_value": 0.4463, "depth": 11}
											if obj[8]>0.0:
												# {"feature": "Children", "instances": 11, "metric_value": 0.3879, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]<=0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[8]<=0.0:
												# {"feature": "Children", "instances": 11, "metric_value": 0.4909, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]<=0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[10]<=0.0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[4]>6:
									# {"feature": "Bar", "instances": 6, "metric_value": 0.4, "depth": 9}
									if obj[8]<=1.0:
										# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.3, "depth": 10}
										if obj[10]<=0.0:
											# {"feature": "Children", "instances": 4, "metric_value": 0.25, "depth": 11}
											if obj[5]>0:
												return 'False'
											elif obj[5]<=0:
												# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[10]>0.0:
											return 'True'
										else: return 'True'
									elif obj[8]>1.0:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					elif obj[6]<=1:
						# {"feature": "Bar", "instances": 522, "metric_value": 0.4308, "depth": 6}
						if obj[8]<=0.0:
							# {"feature": "Time", "instances": 283, "metric_value": 0.453, "depth": 7}
							if obj[1]<=2:
								# {"feature": "Gender", "instances": 163, "metric_value": 0.4818, "depth": 8}
								if obj[3]>0:
									# {"feature": "Occupation", "instances": 112, "metric_value": 0.4703, "depth": 9}
									if obj[7]<=12:
										# {"feature": "Age", "instances": 97, "metric_value": 0.483, "depth": 10}
										if obj[4]>0:
											# {"feature": "Restaurant20to50", "instances": 85, "metric_value": 0.4902, "depth": 11}
											if obj[10]<=1.0:
												# {"feature": "Children", "instances": 70, "metric_value": 0.5, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 46, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[5]<=0:
													# {"feature": "Direction_same", "instances": 24, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[10]>1.0:
												# {"feature": "Children", "instances": 15, "metric_value": 0.3889, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 12, "metric_value": 0.4861, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[4]<=0:
											# {"feature": "Children", "instances": 12, "metric_value": 0.3125, "depth": 11}
											if obj[5]>0:
												# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.125, "depth": 12}
												if obj[10]>-1.0:
													return 'True'
												elif obj[10]<=-1.0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[5]<=0:
												# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.3333, "depth": 12}
												if obj[10]>1.0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[10]<=1.0:
													return 'False'
												else: return 'False'
											else: return 'True'
										else: return 'True'
									elif obj[7]>12:
										# {"feature": "Age", "instances": 15, "metric_value": 0.3143, "depth": 10}
										if obj[4]>1:
											# {"feature": "Children", "instances": 14, "metric_value": 0.3367, "depth": 11}
											if obj[5]<=1:
												# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.3367, "depth": 12}
												if obj[10]<=1.0:
													# {"feature": "Direction_same", "instances": 14, "metric_value": 0.3367, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[4]<=1:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[3]<=0:
									# {"feature": "Restaurant20to50", "instances": 51, "metric_value": 0.4549, "depth": 9}
									if obj[10]<=1.0:
										# {"feature": "Occupation", "instances": 47, "metric_value": 0.4177, "depth": 10}
										if obj[7]<=11:
											# {"feature": "Age", "instances": 38, "metric_value": 0.3916, "depth": 11}
											if obj[4]>0:
												# {"feature": "Children", "instances": 34, "metric_value": 0.437, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 27, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4082, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[4]<=0:
												return 'False'
											else: return 'False'
										elif obj[7]>11:
											# {"feature": "Age", "instances": 9, "metric_value": 0.3333, "depth": 11}
											if obj[4]<=3:
												# {"feature": "Children", "instances": 6, "metric_value": 0.25, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[5]<=0:
													return 'True'
												else: return 'True'
											elif obj[4]>3:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[10]>1.0:
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
								if obj[10]<=1.0:
									# {"feature": "Occupation", "instances": 98, "metric_value": 0.4058, "depth": 9}
									if obj[7]>1:
										# {"feature": "Age", "instances": 71, "metric_value": 0.4479, "depth": 10}
										if obj[4]>2:
											# {"feature": "Children", "instances": 44, "metric_value": 0.4114, "depth": 11}
											if obj[5]>0:
												# {"feature": "Gender", "instances": 24, "metric_value": 0.375, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 16, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[5]<=0:
												# {"feature": "Gender", "instances": 20, "metric_value": 0.4533, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 15, "metric_value": 0.4444, "depth": 13}
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
										elif obj[4]<=2:
											# {"feature": "Children", "instances": 27, "metric_value": 0.4797, "depth": 11}
											if obj[5]>0:
												# {"feature": "Gender", "instances": 21, "metric_value": 0.4444, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 15, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[5]<=0:
												# {"feature": "Gender", "instances": 6, "metric_value": 0.2222, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[7]<=1:
										# {"feature": "Age", "instances": 27, "metric_value": 0.2311, "depth": 10}
										if obj[4]>2:
											# {"feature": "Gender", "instances": 16, "metric_value": 0.1111, "depth": 11}
											if obj[3]>0:
												# {"feature": "Children", "instances": 9, "metric_value": 0.1975, "depth": 12}
												if obj[5]<=1:
													# {"feature": "Direction_same", "instances": 9, "metric_value": 0.1975, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]<=0:
												return 'True'
											else: return 'True'
										elif obj[4]<=2:
											# {"feature": "Gender", "instances": 11, "metric_value": 0.3818, "depth": 11}
											if obj[3]>0:
												# {"feature": "Children", "instances": 10, "metric_value": 0.42, "depth": 12}
												if obj[5]<=1:
													# {"feature": "Direction_same", "instances": 10, "metric_value": 0.42, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[10]>1.0:
									# {"feature": "Age", "instances": 22, "metric_value": 0.1455, "depth": 9}
									if obj[4]<=2:
										return 'True'
									elif obj[4]>2:
										# {"feature": "Children", "instances": 10, "metric_value": 0.275, "depth": 10}
										if obj[5]>0:
											# {"feature": "Occupation", "instances": 8, "metric_value": 0.1875, "depth": 11}
											if obj[7]<=1:
												# {"feature": "Gender", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[3]<=1:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[7]>1:
												return 'True'
											else: return 'True'
										elif obj[5]<=0:
											# {"feature": "Gender", "instances": 2, "metric_value": 0.0, "depth": 11}
											if obj[3]>0:
												return 'True'
											elif obj[3]<=0:
												return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[8]>0.0:
							# {"feature": "Age", "instances": 239, "metric_value": 0.372, "depth": 7}
							if obj[4]<=3:
								# {"feature": "Restaurant20to50", "instances": 154, "metric_value": 0.3166, "depth": 8}
								if obj[10]>-1.0:
									# {"feature": "Occupation", "instances": 147, "metric_value": 0.3001, "depth": 9}
									if obj[7]<=17:
										# {"feature": "Time", "instances": 132, "metric_value": 0.3319, "depth": 10}
										if obj[1]<=3:
											# {"feature": "Gender", "instances": 90, "metric_value": 0.3049, "depth": 11}
											if obj[3]>0:
												# {"feature": "Children", "instances": 49, "metric_value": 0.2704, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 25, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]<=0:
													# {"feature": "Direction_same", "instances": 24, "metric_value": 0.2188, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Children", "instances": 41, "metric_value": 0.3425, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 28, "metric_value": 0.3367, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 13, "metric_value": 0.355, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[1]>3:
											# {"feature": "Gender", "instances": 42, "metric_value": 0.373, "depth": 11}
											if obj[3]>0:
												# {"feature": "Children", "instances": 24, "metric_value": 0.4306, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 12, "metric_value": 0.4861, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]<=0:
													# {"feature": "Direction_same", "instances": 12, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Children", "instances": 18, "metric_value": 0.275, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 10, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.2188, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[7]>17:
										return 'True'
									else: return 'True'
								elif obj[10]<=-1.0:
									# {"feature": "Time", "instances": 7, "metric_value": 0.4048, "depth": 9}
									if obj[1]<=2:
										# {"feature": "Gender", "instances": 4, "metric_value": 0.375, "depth": 10}
										if obj[3]<=1:
											# {"feature": "Children", "instances": 4, "metric_value": 0.375, "depth": 11}
											if obj[5]<=1:
												# {"feature": "Occupation", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[7]<=5:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[1]>2:
										# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[3]<=1:
											# {"feature": "Children", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[5]<=1:
												# {"feature": "Occupation", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[7]<=5:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[4]>3:
								# {"feature": "Time", "instances": 85, "metric_value": 0.4298, "depth": 8}
								if obj[1]<=3:
									# {"feature": "Children", "instances": 66, "metric_value": 0.4014, "depth": 9}
									if obj[5]<=0:
										# {"feature": "Occupation", "instances": 49, "metric_value": 0.4285, "depth": 10}
										if obj[7]>5:
											# {"feature": "Gender", "instances": 30, "metric_value": 0.384, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Restaurant20to50", "instances": 25, "metric_value": 0.3647, "depth": 12}
												if obj[10]>0.0:
													# {"feature": "Direction_same", "instances": 17, "metric_value": 0.3599, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[10]<=0.0:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.48, "depth": 12}
												if obj[10]<=2.0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[7]<=5:
											# {"feature": "Restaurant20to50", "instances": 19, "metric_value": 0.4719, "depth": 11}
											if obj[10]<=1.0:
												# {"feature": "Gender", "instances": 15, "metric_value": 0.4308, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 13, "metric_value": 0.497, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											elif obj[10]>1.0:
												# {"feature": "Gender", "instances": 4, "metric_value": 0.0, "depth": 12}
												if obj[3]<=0:
													return 'True'
												elif obj[3]>0:
													return 'False'
												else: return 'False'
											else: return 'True'
										else: return 'True'
									elif obj[5]>0:
										# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.2773, "depth": 10}
										if obj[10]>0.0:
											# {"feature": "Gender", "instances": 14, "metric_value": 0.329, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Occupation", "instances": 11, "metric_value": 0.297, "depth": 12}
												if obj[7]<=1:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.2778, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[7]>1:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Occupation", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[7]<=19:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[10]<=0.0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[1]>3:
									# {"feature": "Restaurant20to50", "instances": 19, "metric_value": 0.4145, "depth": 9}
									if obj[10]>0.0:
										# {"feature": "Children", "instances": 16, "metric_value": 0.4667, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Occupation", "instances": 15, "metric_value": 0.4889, "depth": 11}
											if obj[7]<=12:
												# {"feature": "Gender", "instances": 12, "metric_value": 0.4815, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4938, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[7]>12:
												# {"feature": "Gender", "instances": 3, "metric_value": 0.3333, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[5]>0:
											return 'True'
										else: return 'True'
									elif obj[10]<=0.0:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[12]>2:
				# {"feature": "Time", "instances": 307, "metric_value": 0.454, "depth": 4}
				if obj[1]>0:
					# {"feature": "Education", "instances": 255, "metric_value": 0.4745, "depth": 5}
					if obj[6]<=2:
						# {"feature": "Bar", "instances": 207, "metric_value": 0.4639, "depth": 6}
						if obj[8]<=0.0:
							# {"feature": "Age", "instances": 109, "metric_value": 0.4815, "depth": 7}
							if obj[4]<=5:
								# {"feature": "Occupation", "instances": 88, "metric_value": 0.4863, "depth": 8}
								if obj[7]<=22:
									# {"feature": "Gender", "instances": 86, "metric_value": 0.4897, "depth": 9}
									if obj[3]>0:
										# {"feature": "Children", "instances": 48, "metric_value": 0.4841, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Restaurant20to50", "instances": 27, "metric_value": 0.4815, "depth": 11}
											if obj[10]<=1.0:
												# {"feature": "Passanger", "instances": 24, "metric_value": 0.4861, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Direction_same", "instances": 24, "metric_value": 0.4861, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[10]>1.0:
												# {"feature": "Passanger", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[5]>0:
											# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.4683, "depth": 11}
											if obj[10]>0.0:
												# {"feature": "Passanger", "instances": 12, "metric_value": 0.4861, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Direction_same", "instances": 12, "metric_value": 0.4861, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[10]<=0.0:
												# {"feature": "Passanger", "instances": 9, "metric_value": 0.4444, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[3]<=0:
										# {"feature": "Restaurant20to50", "instances": 38, "metric_value": 0.439, "depth": 10}
										if obj[10]>0.0:
											# {"feature": "Children", "instances": 30, "metric_value": 0.4795, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Passanger", "instances": 22, "metric_value": 0.4835, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Direction_same", "instances": 22, "metric_value": 0.4835, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[5]>0:
												# {"feature": "Passanger", "instances": 8, "metric_value": 0.4688, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.4688, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[10]<=0.0:
											# {"feature": "Children", "instances": 8, "metric_value": 0.1667, "depth": 11}
											if obj[5]>0:
												return 'True'
											elif obj[5]<=0:
												# {"feature": "Passanger", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[7]>22:
									return 'False'
								else: return 'False'
							elif obj[4]>5:
								# {"feature": "Occupation", "instances": 21, "metric_value": 0.2245, "depth": 8}
								if obj[7]<=9:
									# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.1071, "depth": 9}
									if obj[10]<=1.0:
										return 'False'
									elif obj[10]>1.0:
										# {"feature": "Gender", "instances": 4, "metric_value": 0.25, "depth": 10}
										if obj[3]>0:
											return 'False'
										elif obj[3]<=0:
											# {"feature": "Passanger", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[5]<=1:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[7]>9:
									# {"feature": "Gender", "instances": 7, "metric_value": 0.1905, "depth": 9}
									if obj[3]<=0:
										return 'True'
									elif obj[3]>0:
										# {"feature": "Passanger", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Children", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[5]<=1:
												# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=1.0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'False'
						elif obj[8]>0.0:
							# {"feature": "Occupation", "instances": 98, "metric_value": 0.3936, "depth": 7}
							if obj[7]>1:
								# {"feature": "Age", "instances": 83, "metric_value": 0.3527, "depth": 8}
								if obj[4]<=3:
									# {"feature": "Children", "instances": 46, "metric_value": 0.2499, "depth": 9}
									if obj[5]<=0:
										# {"feature": "Gender", "instances": 29, "metric_value": 0.1826, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.1212, "depth": 11}
											if obj[10]<=1.0:
												# {"feature": "Passanger", "instances": 11, "metric_value": 0.1653, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Direction_same", "instances": 11, "metric_value": 0.1653, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[10]>1.0:
												return 'False'
											else: return 'False'
										elif obj[3]>0:
											# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.2251, "depth": 11}
											if obj[10]<=1.0:
												# {"feature": "Passanger", "instances": 11, "metric_value": 0.1653, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Direction_same", "instances": 11, "metric_value": 0.1653, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[10]>1.0:
												# {"feature": "Passanger", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[5]>0:
										# {"feature": "Gender", "instances": 17, "metric_value": 0.249, "depth": 10}
										if obj[3]>0:
											# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.1389, "depth": 11}
											if obj[10]>1.0:
												# {"feature": "Passanger", "instances": 6, "metric_value": 0.2778, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.2778, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[10]<=1.0:
												return 'False'
											else: return 'False'
										elif obj[3]<=0:
											# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.4667, "depth": 11}
											if obj[10]<=1.0:
												# {"feature": "Passanger", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[10]>1.0:
												# {"feature": "Passanger", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'False'
								elif obj[4]>3:
									# {"feature": "Restaurant20to50", "instances": 37, "metric_value": 0.434, "depth": 9}
									if obj[10]<=1.0:
										# {"feature": "Gender", "instances": 27, "metric_value": 0.4118, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Children", "instances": 19, "metric_value": 0.385, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Passanger", "instances": 14, "metric_value": 0.4082, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Direction_same", "instances": 14, "metric_value": 0.4082, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[5]>0:
												# {"feature": "Passanger", "instances": 5, "metric_value": 0.32, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[3]>0:
											# {"feature": "Children", "instances": 8, "metric_value": 0.4667, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Passanger", "instances": 5, "metric_value": 0.48, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[5]>0:
												# {"feature": "Passanger", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[10]>1.0:
										# {"feature": "Children", "instances": 10, "metric_value": 0.4, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Passanger", "instances": 8, "metric_value": 0.5, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Gender", "instances": 8, "metric_value": 0.5, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[5]>0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[7]<=1:
								# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.4286, "depth": 8}
								if obj[10]>0.0:
									# {"feature": "Gender", "instances": 14, "metric_value": 0.3937, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Age", "instances": 9, "metric_value": 0.2963, "depth": 10}
										if obj[4]<=1:
											# {"feature": "Passanger", "instances": 6, "metric_value": 0.4444, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Children", "instances": 6, "metric_value": 0.4444, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
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
												# {"feature": "Children", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[4]>1:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[10]<=0.0:
									return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'False'
					elif obj[6]>2:
						# {"feature": "Occupation", "instances": 48, "metric_value": 0.407, "depth": 6}
						if obj[7]>4:
							# {"feature": "Age", "instances": 29, "metric_value": 0.4708, "depth": 7}
							if obj[4]<=3:
								# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.4167, "depth": 8}
								if obj[10]>-1.0:
									# {"feature": "Bar", "instances": 15, "metric_value": 0.4074, "depth": 9}
									if obj[8]>0.0:
										# {"feature": "Children", "instances": 9, "metric_value": 0.4167, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Gender", "instances": 8, "metric_value": 0.375, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Passanger", "instances": 6, "metric_value": 0.5, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]>0:
												return 'True'
											else: return 'True'
										elif obj[5]>0:
											return 'False'
										else: return 'False'
									elif obj[8]<=0.0:
										# {"feature": "Gender", "instances": 6, "metric_value": 0.25, "depth": 10}
										if obj[3]>0:
											# {"feature": "Children", "instances": 4, "metric_value": 0.25, "depth": 11}
											if obj[5]<=0:
												return 'True'
											elif obj[5]>0:
												# {"feature": "Passanger", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[10]<=-1.0:
									return 'False'
								else: return 'False'
							elif obj[4]>3:
								# {"feature": "Bar", "instances": 13, "metric_value": 0.3547, "depth": 8}
								if obj[8]<=0.0:
									# {"feature": "Children", "instances": 9, "metric_value": 0.2667, "depth": 9}
									if obj[5]>0:
										# {"feature": "Passanger", "instances": 5, "metric_value": 0.48, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Gender", "instances": 5, "metric_value": 0.48, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.48, "depth": 12}
												if obj[10]<=2.0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[5]<=0:
										return 'False'
									else: return 'False'
								elif obj[8]>0.0:
									# {"feature": "Children", "instances": 4, "metric_value": 0.25, "depth": 9}
									if obj[5]<=0:
										return 'True'
									elif obj[5]>0:
										# {"feature": "Gender", "instances": 2, "metric_value": 0.0, "depth": 10}
										if obj[3]>0:
											return 'True'
										elif obj[3]<=0:
											return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[7]<=4:
							# {"feature": "Age", "instances": 19, "metric_value": 0.2241, "depth": 7}
							if obj[4]>1:
								# {"feature": "Children", "instances": 14, "metric_value": 0.127, "depth": 8}
								if obj[5]<=0:
									# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.1852, "depth": 9}
									if obj[10]>0.0:
										# {"feature": "Gender", "instances": 6, "metric_value": 0.2667, "depth": 10}
										if obj[3]>0:
											# {"feature": "Bar", "instances": 5, "metric_value": 0.3, "depth": 11}
											if obj[8]<=0.0:
												# {"feature": "Passanger", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[8]>0.0:
												return 'True'
											else: return 'True'
										elif obj[3]<=0:
											return 'True'
										else: return 'True'
									elif obj[10]<=0.0:
										return 'True'
									else: return 'True'
								elif obj[5]>0:
									return 'True'
								else: return 'True'
							elif obj[4]<=1:
								# {"feature": "Gender", "instances": 5, "metric_value": 0.2667, "depth": 8}
								if obj[3]>0:
									# {"feature": "Passanger", "instances": 3, "metric_value": 0.4444, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Children", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[5]<=1:
											# {"feature": "Bar", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[8]<=1.0:
												# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0.0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
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
							if obj[7]>1:
								# {"feature": "Education", "instances": 14, "metric_value": 0.0952, "depth": 8}
								if obj[6]>0:
									return 'False'
								elif obj[6]<=0:
									# {"feature": "Bar", "instances": 3, "metric_value": 0.0, "depth": 9}
									if obj[8]>0.0:
										return 'False'
									elif obj[8]<=0.0:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[7]<=1:
								# {"feature": "Children", "instances": 5, "metric_value": 0.4, "depth": 8}
								if obj[5]<=0:
									# {"feature": "Education", "instances": 4, "metric_value": 0.3333, "depth": 9}
									if obj[6]>0:
										# {"feature": "Gender", "instances": 3, "metric_value": 0.3333, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Bar", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[8]<=1.0:
												# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=1.0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]>0:
											return 'True'
										else: return 'True'
									elif obj[6]<=0:
										return 'False'
									else: return 'False'
								elif obj[5]>0:
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
		elif obj[9]>1.0:
			# {"feature": "Distance", "instances": 2845, "metric_value": 0.4173, "depth": 3}
			if obj[12]<=2:
				# {"feature": "Passanger", "instances": 2564, "metric_value": 0.4036, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Occupation", "instances": 1682, "metric_value": 0.433, "depth": 5}
					if obj[7]<=18.296160208955353:
						# {"feature": "Age", "instances": 1558, "metric_value": 0.4406, "depth": 6}
						if obj[4]>0:
							# {"feature": "Bar", "instances": 1347, "metric_value": 0.4317, "depth": 7}
							if obj[8]>0.0:
								# {"feature": "Time", "instances": 943, "metric_value": 0.4423, "depth": 8}
								if obj[1]<=3:
									# {"feature": "Restaurant20to50", "instances": 775, "metric_value": 0.4532, "depth": 9}
									if obj[10]<=1.0:
										# {"feature": "Children", "instances": 424, "metric_value": 0.469, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Direction_same", "instances": 272, "metric_value": 0.4833, "depth": 11}
											if obj[11]>0:
												# {"feature": "Education", "instances": 144, "metric_value": 0.4609, "depth": 12}
												if obj[6]<=2:
													# {"feature": "Gender", "instances": 124, "metric_value": 0.4578, "depth": 13}
													if obj[3]<=0:
														return 'True'
													elif obj[3]>0:
														return 'True'
													else: return 'True'
												elif obj[6]>2:
													# {"feature": "Gender", "instances": 20, "metric_value": 0.4235, "depth": 13}
													if obj[3]<=0:
														return 'False'
													elif obj[3]>0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[11]<=0:
												# {"feature": "Education", "instances": 128, "metric_value": 0.4821, "depth": 12}
												if obj[6]<=3:
													# {"feature": "Gender", "instances": 121, "metric_value": 0.4958, "depth": 13}
													if obj[3]<=0:
														return 'True'
													elif obj[3]>0:
														return 'True'
													else: return 'True'
												elif obj[6]>3:
													# {"feature": "Gender", "instances": 7, "metric_value": 0.2449, "depth": 13}
													if obj[3]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[5]>0:
											# {"feature": "Gender", "instances": 152, "metric_value": 0.4329, "depth": 11}
											if obj[3]>0:
												# {"feature": "Education", "instances": 98, "metric_value": 0.4633, "depth": 12}
												if obj[6]>0:
													# {"feature": "Direction_same", "instances": 80, "metric_value": 0.4541, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[6]<=0:
													# {"feature": "Direction_same", "instances": 18, "metric_value": 0.4706, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Education", "instances": 54, "metric_value": 0.3611, "depth": 12}
												if obj[6]>0:
													# {"feature": "Direction_same", "instances": 52, "metric_value": 0.3719, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[6]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[10]>1.0:
										# {"feature": "Education", "instances": 351, "metric_value": 0.4271, "depth": 10}
										if obj[6]>0:
											# {"feature": "Direction_same", "instances": 268, "metric_value": 0.437, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Gender", "instances": 149, "metric_value": 0.4711, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Children", "instances": 82, "metric_value": 0.4497, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Children", "instances": 67, "metric_value": 0.4944, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[11]>0:
												# {"feature": "Children", "instances": 119, "metric_value": 0.3793, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Gender", "instances": 89, "metric_value": 0.4024, "depth": 13}
													if obj[3]>0:
														return 'True'
													elif obj[3]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Gender", "instances": 30, "metric_value": 0.26, "depth": 13}
													if obj[3]<=0:
														return 'True'
													elif obj[3]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[6]<=0:
											# {"feature": "Direction_same", "instances": 83, "metric_value": 0.3607, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Gender", "instances": 50, "metric_value": 0.3168, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Children", "instances": 25, "metric_value": 0.2612, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Children", "instances": 25, "metric_value": 0.3627, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[11]>0:
												# {"feature": "Gender", "instances": 33, "metric_value": 0.4222, "depth": 12}
												if obj[3]>0:
													# {"feature": "Children", "instances": 17, "metric_value": 0.4151, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													# {"feature": "Children", "instances": 16, "metric_value": 0.4295, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[1]>3:
									# {"feature": "Restaurant20to50", "instances": 168, "metric_value": 0.378, "depth": 9}
									if obj[10]<=3.0:
										# {"feature": "Children", "instances": 164, "metric_value": 0.3715, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Education", "instances": 109, "metric_value": 0.3357, "depth": 11}
											if obj[6]>1:
												# {"feature": "Gender", "instances": 65, "metric_value": 0.2808, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 38, "metric_value": 0.2659, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 27, "metric_value": 0.3018, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[6]<=1:
												# {"feature": "Gender", "instances": 44, "metric_value": 0.4163, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 24, "metric_value": 0.4132, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 20, "metric_value": 0.42, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[5]>0:
											# {"feature": "Education", "instances": 55, "metric_value": 0.4033, "depth": 11}
											if obj[6]>0:
												# {"feature": "Gender", "instances": 44, "metric_value": 0.4625, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 24, "metric_value": 0.4688, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 20, "metric_value": 0.455, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[6]<=0:
												# {"feature": "Gender", "instances": 11, "metric_value": 0.1558, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.2449, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[10]>3.0:
										# {"feature": "Children", "instances": 4, "metric_value": 0.3333, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Education", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[6]<=4:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[5]>0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[8]<=0.0:
								# {"feature": "Time", "instances": 404, "metric_value": 0.3985, "depth": 8}
								if obj[1]<=2:
									# {"feature": "Restaurant20to50", "instances": 282, "metric_value": 0.3784, "depth": 9}
									if obj[10]>-1.0:
										# {"feature": "Gender", "instances": 278, "metric_value": 0.3819, "depth": 10}
										if obj[3]>0:
											# {"feature": "Education", "instances": 181, "metric_value": 0.4021, "depth": 11}
											if obj[6]<=2:
												# {"feature": "Children", "instances": 141, "metric_value": 0.3836, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 98, "metric_value": 0.3591, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[5]<=0:
													# {"feature": "Direction_same", "instances": 43, "metric_value": 0.4333, "depth": 13}
													if obj[11]>0:
														return 'True'
													elif obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[6]>2:
												# {"feature": "Children", "instances": 40, "metric_value": 0.4074, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 23, "metric_value": 0.3398, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 17, "metric_value": 0.4941, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[3]<=0:
											# {"feature": "Direction_same", "instances": 97, "metric_value": 0.3348, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Education", "instances": 59, "metric_value": 0.3747, "depth": 12}
												if obj[6]<=3:
													# {"feature": "Children", "instances": 57, "metric_value": 0.387, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												elif obj[6]>3:
													return 'True'
												else: return 'True'
											elif obj[11]>0:
												# {"feature": "Children", "instances": 38, "metric_value": 0.2375, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Education", "instances": 26, "metric_value": 0.1348, "depth": 13}
													if obj[6]<=0:
														return 'True'
													elif obj[6]>0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Education", "instances": 12, "metric_value": 0.4333, "depth": 13}
													if obj[6]>0:
														return 'True'
													elif obj[6]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[10]<=-1.0:
										return 'True'
									else: return 'True'
								elif obj[1]>2:
									# {"feature": "Children", "instances": 122, "metric_value": 0.43, "depth": 9}
									if obj[5]>0:
										# {"feature": "Restaurant20to50", "instances": 72, "metric_value": 0.454, "depth": 10}
										if obj[10]>0.0:
											# {"feature": "Education", "instances": 70, "metric_value": 0.4484, "depth": 11}
											if obj[6]<=2:
												# {"feature": "Direction_same", "instances": 58, "metric_value": 0.4312, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Gender", "instances": 51, "metric_value": 0.4532, "depth": 13}
													if obj[3]>0:
														return 'True'
													elif obj[3]<=0:
														return 'True'
													else: return 'True'
												elif obj[11]>0:
													# {"feature": "Gender", "instances": 7, "metric_value": 0.2381, "depth": 13}
													if obj[3]>0:
														return 'True'
													elif obj[3]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[6]>2:
												# {"feature": "Direction_same", "instances": 12, "metric_value": 0.4583, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Gender", "instances": 8, "metric_value": 0.5, "depth": 13}
													if obj[3]>0:
														return 'False'
													elif obj[3]<=0:
														return 'True'
													else: return 'True'
												elif obj[11]>0:
													# {"feature": "Gender", "instances": 4, "metric_value": 0.25, "depth": 13}
													if obj[3]>0:
														return 'False'
													elif obj[3]<=0:
														return 'True'
													else: return 'True'
												else: return 'False'
											else: return 'False'
										elif obj[10]<=0.0:
											return 'False'
										else: return 'False'
									elif obj[5]<=0:
										# {"feature": "Gender", "instances": 50, "metric_value": 0.3549, "depth": 10}
										if obj[3]>0:
											# {"feature": "Education", "instances": 26, "metric_value": 0.4028, "depth": 11}
											if obj[6]<=2:
												# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.4286, "depth": 12}
												if obj[10]>0.0:
													# {"feature": "Direction_same", "instances": 14, "metric_value": 0.4589, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[10]<=0.0:
													return 'False'
												else: return 'False'
											elif obj[6]>2:
												# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.2909, "depth": 12}
												if obj[10]>0.0:
													# {"feature": "Direction_same", "instances": 10, "metric_value": 0.3167, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[10]<=0.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]<=0:
											# {"feature": "Direction_same", "instances": 24, "metric_value": 0.2344, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.1071, "depth": 12}
												if obj[10]>0.0:
													return 'True'
												elif obj[10]<=0.0:
													# {"feature": "Education", "instances": 7, "metric_value": 0.2449, "depth": 13}
													if obj[6]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[11]>0:
												# {"feature": "Education", "instances": 8, "metric_value": 0.375, "depth": 12}
												if obj[6]<=0:
													# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.4, "depth": 13}
													if obj[10]>0.0:
														return 'False'
													elif obj[10]<=0.0:
														return 'True'
													else: return 'True'
												elif obj[6]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[4]<=0:
							# {"feature": "Education", "instances": 211, "metric_value": 0.465, "depth": 7}
							if obj[6]<=3:
								# {"feature": "Restaurant20to50", "instances": 180, "metric_value": 0.477, "depth": 8}
								if obj[10]<=2.0:
									# {"feature": "Bar", "instances": 143, "metric_value": 0.4689, "depth": 9}
									if obj[8]<=3.0:
										# {"feature": "Gender", "instances": 136, "metric_value": 0.4722, "depth": 10}
										if obj[3]>0:
											# {"feature": "Time", "instances": 98, "metric_value": 0.4671, "depth": 11}
											if obj[1]<=2:
												# {"feature": "Children", "instances": 63, "metric_value": 0.4522, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 49, "metric_value": 0.4647, "depth": 13}
													if obj[11]>0:
														return 'True'
													elif obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]<=0:
													# {"feature": "Direction_same", "instances": 14, "metric_value": 0.4048, "depth": 13}
													if obj[11]>0:
														return 'True'
													elif obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[1]>2:
												# {"feature": "Children", "instances": 35, "metric_value": 0.4663, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 29, "metric_value": 0.4698, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[5]<=0:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[3]<=0:
											# {"feature": "Children", "instances": 38, "metric_value": 0.41, "depth": 11}
											if obj[5]>0:
												# {"feature": "Time", "instances": 19, "metric_value": 0.2679, "depth": 12}
												if obj[1]>0:
													# {"feature": "Direction_same", "instances": 11, "metric_value": 0.4416, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[1]<=0:
													return 'False'
												else: return 'False'
											elif obj[5]<=0:
												# {"feature": "Direction_same", "instances": 19, "metric_value": 0.393, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Time", "instances": 15, "metric_value": 0.4308, "depth": 13}
													if obj[1]>0:
														return 'True'
													elif obj[1]<=0:
														return 'False'
													else: return 'False'
												elif obj[11]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[8]>3.0:
										return 'True'
									else: return 'True'
								elif obj[10]>2.0:
									# {"feature": "Gender", "instances": 37, "metric_value": 0.3338, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Time", "instances": 21, "metric_value": 0.4233, "depth": 10}
										if obj[1]<=3:
											# {"feature": "Direction_same", "instances": 18, "metric_value": 0.4333, "depth": 11}
											if obj[11]>0:
												# {"feature": "Children", "instances": 10, "metric_value": 0.4444, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Bar", "instances": 9, "metric_value": 0.4938, "depth": 13}
													if obj[8]<=2.0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													return 'True'
												else: return 'True'
											elif obj[11]<=0:
												# {"feature": "Children", "instances": 8, "metric_value": 0.25, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Bar", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[8]<=2.0:
														return 'False'
													else: return 'False'
												elif obj[5]>0:
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
											if obj[8]<=2.0:
												# {"feature": "Children", "instances": 3, "metric_value": 0.0, "depth": 12}
												if obj[5]>0:
													return 'False'
												elif obj[5]<=0:
													return 'True'
												else: return 'True'
											elif obj[8]>2.0:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[6]>3:
								# {"feature": "Time", "instances": 31, "metric_value": 0.2525, "depth": 8}
								if obj[1]<=3:
									# {"feature": "Gender", "instances": 23, "metric_value": 0.323, "depth": 9}
									if obj[3]>0:
										# {"feature": "Bar", "instances": 14, "metric_value": 0.2041, "depth": 10}
										if obj[8]>0.0:
											# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4048, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Children", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[10]<=1.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[11]>0:
												# {"feature": "Children", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[10]<=1.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[8]<=0.0:
											return 'True'
										else: return 'True'
									elif obj[3]<=0:
										# {"feature": "Direction_same", "instances": 9, "metric_value": 0.381, "depth": 10}
										if obj[11]<=0:
											# {"feature": "Bar", "instances": 7, "metric_value": 0.4762, "depth": 11}
											if obj[8]<=0.0:
												# {"feature": "Children", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[5]<=1:
													# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[10]<=1.0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[8]>0.0:
												# {"feature": "Children", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[5]<=1:
													# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[10]<=4.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[11]>0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[1]>3:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[7]>18.296160208955353:
						# {"feature": "Age", "instances": 124, "metric_value": 0.2839, "depth": 6}
						if obj[4]>0:
							# {"feature": "Bar", "instances": 98, "metric_value": 0.3358, "depth": 7}
							if obj[8]<=2.0:
								# {"feature": "Time", "instances": 84, "metric_value": 0.2981, "depth": 8}
								if obj[1]<=1:
									# {"feature": "Children", "instances": 53, "metric_value": 0.3541, "depth": 9}
									if obj[5]>0:
										# {"feature": "Restaurant20to50", "instances": 30, "metric_value": 0.2692, "depth": 10}
										if obj[10]>0.0:
											# {"feature": "Gender", "instances": 26, "metric_value": 0.3077, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Education", "instances": 13, "metric_value": 0.2393, "depth": 12}
												if obj[6]<=1:
													# {"feature": "Direction_same", "instances": 9, "metric_value": 0.3016, "depth": 13}
													if obj[11]>0:
														return 'True'
													elif obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[6]>1:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Education", "instances": 13, "metric_value": 0.348, "depth": 12}
												if obj[6]>1:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.381, "depth": 13}
													if obj[11]>0:
														return 'True'
													elif obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[6]<=1:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.25, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[10]<=0.0:
											return 'True'
										else: return 'True'
									elif obj[5]<=0:
										# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.4174, "depth": 10}
										if obj[10]<=2.0:
											# {"feature": "Direction_same", "instances": 20, "metric_value": 0.4283, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Gender", "instances": 11, "metric_value": 0.4606, "depth": 12}
												if obj[3]>0:
													# {"feature": "Education", "instances": 6, "metric_value": 0.4444, "depth": 13}
													if obj[6]<=1:
														return 'False'
													elif obj[6]>1:
														return 'False'
													else: return 'False'
												elif obj[3]<=0:
													# {"feature": "Education", "instances": 5, "metric_value": 0.4667, "depth": 13}
													if obj[6]<=0:
														return 'True'
													elif obj[6]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[11]>0:
												# {"feature": "Education", "instances": 9, "metric_value": 0.2222, "depth": 12}
												if obj[6]<=2:
													return 'True'
												elif obj[6]>2:
													# {"feature": "Gender", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[3]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[10]>2.0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[1]>1:
									# {"feature": "Direction_same", "instances": 31, "metric_value": 0.1628, "depth": 9}
									if obj[11]<=0:
										# {"feature": "Restaurant20to50", "instances": 28, "metric_value": 0.122, "depth": 10}
										if obj[10]>0.0:
											# {"feature": "Children", "instances": 24, "metric_value": 0.075, "depth": 11}
											if obj[5]>0:
												return 'True'
											elif obj[5]<=0:
												# {"feature": "Education", "instances": 10, "metric_value": 0.1333, "depth": 12}
												if obj[6]<=2:
													return 'True'
												elif obj[6]>2:
													# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[3]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[10]<=0.0:
											# {"feature": "Gender", "instances": 4, "metric_value": 0.375, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Children", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[5]<=1:
													# {"feature": "Education", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[6]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[11]>0:
										# {"feature": "Gender", "instances": 3, "metric_value": 0.3333, "depth": 10}
										if obj[3]>0:
											# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[5]<=1:
												# {"feature": "Education", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[6]<=3:
													# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[10]<=1.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[8]>2.0:
								# {"feature": "Time", "instances": 14, "metric_value": 0.3636, "depth": 8}
								if obj[1]<=3:
									# {"feature": "Direction_same", "instances": 11, "metric_value": 0.3117, "depth": 9}
									if obj[11]>0:
										# {"feature": "Education", "instances": 7, "metric_value": 0.4762, "depth": 10}
										if obj[6]>0:
											# {"feature": "Gender", "instances": 4, "metric_value": 0.5, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Children", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[10]<=2.0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[6]<=0:
											# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Children", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[10]<=2.0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[11]<=0:
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
						if obj[8]<=3.0:
							# {"feature": "Children", "instances": 507, "metric_value": 0.2654, "depth": 7}
							if obj[5]<=0:
								# {"feature": "Occupation", "instances": 322, "metric_value": 0.2097, "depth": 8}
								if obj[7]<=13:
									# {"feature": "Restaurant20to50", "instances": 277, "metric_value": 0.2344, "depth": 9}
									if obj[10]<=2.0:
										# {"feature": "Age", "instances": 258, "metric_value": 0.22, "depth": 10}
										if obj[4]<=5:
											# {"feature": "Gender", "instances": 234, "metric_value": 0.2032, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Education", "instances": 143, "metric_value": 0.2287, "depth": 12}
												if obj[6]<=1:
													# {"feature": "Direction_same", "instances": 76, "metric_value": 0.1884, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[6]>1:
													# {"feature": "Direction_same", "instances": 67, "metric_value": 0.2744, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Education", "instances": 91, "metric_value": 0.1516, "depth": 12}
												if obj[6]>0:
													# {"feature": "Direction_same", "instances": 65, "metric_value": 0.088, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[6]<=0:
													# {"feature": "Direction_same", "instances": 26, "metric_value": 0.3107, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[4]>5:
											# {"feature": "Gender", "instances": 24, "metric_value": 0.3254, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Education", "instances": 21, "metric_value": 0.2778, "depth": 12}
												if obj[6]<=1:
													# {"feature": "Direction_same", "instances": 12, "metric_value": 0.1528, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[6]>1:
													# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Education", "instances": 3, "metric_value": 0.0, "depth": 12}
												if obj[6]<=0:
													return 'False'
												elif obj[6]>0:
													return 'True'
												else: return 'True'
											else: return 'False'
										else: return 'True'
									elif obj[10]>2.0:
										# {"feature": "Gender", "instances": 19, "metric_value": 0.3462, "depth": 10}
										if obj[3]>0:
											# {"feature": "Age", "instances": 10, "metric_value": 0.3429, "depth": 11}
											if obj[4]<=1:
												# {"feature": "Education", "instances": 7, "metric_value": 0.4286, "depth": 12}
												if obj[6]>2:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[6]<=2:
													return 'False'
												else: return 'False'
											elif obj[4]>1:
												return 'True'
											else: return 'True'
										elif obj[3]<=0:
											# {"feature": "Age", "instances": 9, "metric_value": 0.1667, "depth": 11}
											if obj[4]<=3:
												return 'True'
											elif obj[4]>3:
												# {"feature": "Education", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[6]<=0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[7]>13:
									# {"feature": "Restaurant20to50", "instances": 45, "metric_value": 0.0423, "depth": 9}
									if obj[10]<=1.0:
										return 'True'
									elif obj[10]>1.0:
										# {"feature": "Age", "instances": 21, "metric_value": 0.0884, "depth": 10}
										if obj[4]>0:
											# {"feature": "Education", "instances": 14, "metric_value": 0.127, "depth": 11}
											if obj[6]>2:
												# {"feature": "Gender", "instances": 9, "metric_value": 0.1975, "depth": 12}
												if obj[3]<=1:
													# {"feature": "Direction_same", "instances": 9, "metric_value": 0.1975, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[6]<=2:
												return 'True'
											else: return 'True'
										elif obj[4]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[5]>0:
								# {"feature": "Age", "instances": 185, "metric_value": 0.3502, "depth": 8}
								if obj[4]>2:
									# {"feature": "Occupation", "instances": 102, "metric_value": 0.3887, "depth": 9}
									if obj[7]<=12:
										# {"feature": "Education", "instances": 96, "metric_value": 0.3749, "depth": 10}
										if obj[6]>0:
											# {"feature": "Restaurant20to50", "instances": 66, "metric_value": 0.3298, "depth": 11}
											if obj[10]>0.0:
												# {"feature": "Gender", "instances": 56, "metric_value": 0.3562, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 36, "metric_value": 0.3457, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 20, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[10]<=0.0:
												# {"feature": "Gender", "instances": 10, "metric_value": 0.1714, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.2449, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[6]<=0:
											# {"feature": "Gender", "instances": 30, "metric_value": 0.4407, "depth": 11}
											if obj[3]>0:
												# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.3723, "depth": 12}
												if obj[10]>0.0:
													# {"feature": "Direction_same", "instances": 11, "metric_value": 0.2975, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[10]<=0.0:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4898, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=1.0:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[10]>1.0:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[7]>12:
										# {"feature": "Gender", "instances": 6, "metric_value": 0.3333, "depth": 10}
										if obj[3]>0:
											# {"feature": "Education", "instances": 4, "metric_value": 0.5, "depth": 11}
											if obj[6]<=2:
												# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[10]<=1.0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[3]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[4]<=2:
									# {"feature": "Occupation", "instances": 83, "metric_value": 0.2751, "depth": 9}
									if obj[7]<=12:
										# {"feature": "Education", "instances": 67, "metric_value": 0.3081, "depth": 10}
										if obj[6]<=2:
											# {"feature": "Restaurant20to50", "instances": 44, "metric_value": 0.2443, "depth": 11}
											if obj[10]<=2.0:
												# {"feature": "Gender", "instances": 40, "metric_value": 0.2165, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 27, "metric_value": 0.2524, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 13, "metric_value": 0.142, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[10]>2.0:
												# {"feature": "Gender", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[6]>2:
											# {"feature": "Gender", "instances": 23, "metric_value": 0.3568, "depth": 11}
											if obj[3]>0:
												# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.4167, "depth": 12}
												if obj[10]>0.0:
													# {"feature": "Direction_same", "instances": 12, "metric_value": 0.4861, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[10]<=0.0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.1944, "depth": 12}
												if obj[10]<=1.0:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.2188, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[10]>1.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[7]>12:
										# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.1, "depth": 10}
										if obj[10]<=1.0:
											return 'True'
										elif obj[10]>1.0:
											# {"feature": "Gender", "instances": 5, "metric_value": 0.2667, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Education", "instances": 3, "metric_value": 0.0, "depth": 12}
												if obj[6]<=0:
													return 'True'
												elif obj[6]>0:
													return 'False'
												else: return 'False'
											elif obj[3]>0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[8]>3.0:
							# {"feature": "Restaurant20to50", "instances": 38, "metric_value": 0.4369, "depth": 7}
							if obj[10]>1.0:
								# {"feature": "Occupation", "instances": 22, "metric_value": 0.3463, "depth": 8}
								if obj[7]<=14:
									# {"feature": "Age", "instances": 21, "metric_value": 0.3361, "depth": 9}
									if obj[4]>0:
										# {"feature": "Gender", "instances": 17, "metric_value": 0.3832, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Children", "instances": 10, "metric_value": 0.48, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Education", "instances": 10, "metric_value": 0.48, "depth": 12}
												if obj[6]>0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[6]<=0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]>0:
											# {"feature": "Education", "instances": 7, "metric_value": 0.2381, "depth": 11}
											if obj[6]<=0:
												# {"feature": "Children", "instances": 6, "metric_value": 0.2778, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.2778, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[6]>0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[4]<=0:
										return 'True'
									else: return 'True'
								elif obj[7]>14:
									return 'False'
								else: return 'False'
							elif obj[10]<=1.0:
								# {"feature": "Age", "instances": 16, "metric_value": 0.45, "depth": 8}
								if obj[4]>0:
									# {"feature": "Gender", "instances": 15, "metric_value": 0.4778, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Education", "instances": 12, "metric_value": 0.4857, "depth": 10}
										if obj[6]<=0:
											# {"feature": "Children", "instances": 7, "metric_value": 0.4898, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Occupation", "instances": 7, "metric_value": 0.4898, "depth": 12}
												if obj[7]<=18:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4898, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[6]>0:
											# {"feature": "Children", "instances": 5, "metric_value": 0.48, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Occupation", "instances": 5, "metric_value": 0.48, "depth": 12}
												if obj[7]<=2:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[3]>0:
										# {"feature": "Children", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Education", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[6]<=0:
												# {"feature": "Occupation", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[7]<=7:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
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
							if obj[8]<=3.0:
								# {"feature": "Education", "instances": 182, "metric_value": 0.4334, "depth": 8}
								if obj[6]<=3:
									# {"feature": "Occupation", "instances": 170, "metric_value": 0.4475, "depth": 9}
									if obj[7]>1:
										# {"feature": "Restaurant20to50", "instances": 150, "metric_value": 0.4599, "depth": 10}
										if obj[10]>0.0:
											# {"feature": "Children", "instances": 141, "metric_value": 0.4542, "depth": 11}
											if obj[5]>0:
												# {"feature": "Gender", "instances": 82, "metric_value": 0.4736, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 53, "metric_value": 0.4856, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 29, "metric_value": 0.4518, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[5]<=0:
												# {"feature": "Gender", "instances": 59, "metric_value": 0.4233, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 31, "metric_value": 0.437, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 28, "metric_value": 0.4082, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[10]<=0.0:
											# {"feature": "Gender", "instances": 9, "metric_value": 0.3444, "depth": 11}
											if obj[3]>0:
												# {"feature": "Children", "instances": 5, "metric_value": 0.32, "depth": 12}
												if obj[5]<=1:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[3]<=0:
												# {"feature": "Children", "instances": 4, "metric_value": 0.0, "depth": 12}
												if obj[5]>0:
													return 'True'
												elif obj[5]<=0:
													return 'False'
												else: return 'False'
											else: return 'True'
										else: return 'False'
									elif obj[7]<=1:
										# {"feature": "Restaurant20to50", "instances": 20, "metric_value": 0.3, "depth": 10}
										if obj[10]>0.0:
											# {"feature": "Gender", "instances": 16, "metric_value": 0.375, "depth": 11}
											if obj[3]<=1:
												# {"feature": "Children", "instances": 16, "metric_value": 0.375, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]<=0:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[10]<=0.0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[6]>3:
									# {"feature": "Occupation", "instances": 12, "metric_value": 0.0, "depth": 9}
									if obj[7]>1:
										return 'True'
									elif obj[7]<=1:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[8]>3.0:
								# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.2381, "depth": 8}
								if obj[10]>1.0:
									# {"feature": "Education", "instances": 6, "metric_value": 0.25, "depth": 9}
									if obj[6]>3:
										# {"feature": "Gender", "instances": 4, "metric_value": 0.375, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Children", "instances": 4, "metric_value": 0.375, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Occupation", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[7]<=1:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[6]<=3:
										return 'False'
									else: return 'False'
								elif obj[10]<=1.0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[4]>3:
							# {"feature": "Restaurant20to50", "instances": 148, "metric_value": 0.3203, "depth": 7}
							if obj[10]<=1.0:
								# {"feature": "Gender", "instances": 84, "metric_value": 0.3607, "depth": 8}
								if obj[3]<=0:
									# {"feature": "Bar", "instances": 53, "metric_value": 0.2614, "depth": 9}
									if obj[8]<=1.0:
										# {"feature": "Occupation", "instances": 33, "metric_value": 0.1437, "depth": 10}
										if obj[7]<=7:
											# {"feature": "Education", "instances": 31, "metric_value": 0.1191, "depth": 11}
											if obj[6]<=2:
												# {"feature": "Children", "instances": 26, "metric_value": 0.1415, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 25, "metric_value": 0.1472, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													return 'True'
												else: return 'True'
											elif obj[6]>2:
												return 'True'
											else: return 'True'
										elif obj[7]>7:
											# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[5]<=1:
												# {"feature": "Education", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[6]<=3:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[8]>1.0:
										# {"feature": "Occupation", "instances": 20, "metric_value": 0.3111, "depth": 10}
										if obj[7]>1:
											# {"feature": "Children", "instances": 18, "metric_value": 0.3333, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Education", "instances": 16, "metric_value": 0.3727, "depth": 12}
												if obj[6]>0:
													# {"feature": "Direction_same", "instances": 11, "metric_value": 0.3967, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[6]<=0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[5]>0:
												return 'True'
											else: return 'True'
										elif obj[7]<=1:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[3]>0:
									# {"feature": "Occupation", "instances": 31, "metric_value": 0.4516, "depth": 9}
									if obj[7]>0:
										# {"feature": "Bar", "instances": 28, "metric_value": 0.44, "depth": 10}
										if obj[8]<=2.0:
											# {"feature": "Education", "instances": 25, "metric_value": 0.4753, "depth": 11}
											if obj[6]<=0:
												# {"feature": "Children", "instances": 14, "metric_value": 0.4583, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.4688, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[6]>0:
												# {"feature": "Children", "instances": 11, "metric_value": 0.4621, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.4688, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[8]>2.0:
											return 'True'
										else: return 'True'
									elif obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[10]>1.0:
								# {"feature": "Gender", "instances": 64, "metric_value": 0.205, "depth": 8}
								if obj[3]>0:
									# {"feature": "Bar", "instances": 37, "metric_value": 0.0885, "depth": 9}
									if obj[8]<=2.0:
										# {"feature": "Education", "instances": 34, "metric_value": 0.0546, "depth": 10}
										if obj[6]>0:
											return 'True'
										elif obj[6]<=0:
											# {"feature": "Children", "instances": 14, "metric_value": 0.125, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Occupation", "instances": 8, "metric_value": 0.2, "depth": 12}
												if obj[7]<=7:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[7]>7:
													return 'True'
												else: return 'True'
											elif obj[5]>0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[8]>2.0:
										# {"feature": "Children", "instances": 3, "metric_value": 0.0, "depth": 10}
										if obj[5]<=0:
											return 'True'
										elif obj[5]>0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[3]<=0:
									# {"feature": "Bar", "instances": 27, "metric_value": 0.3333, "depth": 9}
									if obj[8]>0.0:
										# {"feature": "Education", "instances": 24, "metric_value": 0.3632, "depth": 10}
										if obj[6]>0:
											# {"feature": "Occupation", "instances": 19, "metric_value": 0.3218, "depth": 11}
											if obj[7]>7:
												# {"feature": "Children", "instances": 11, "metric_value": 0.3961, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4082, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]<=0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[7]<=7:
												# {"feature": "Children", "instances": 8, "metric_value": 0.2188, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.2188, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[6]<=0:
											# {"feature": "Children", "instances": 5, "metric_value": 0.4, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Occupation", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[7]<=7:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[5]>0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[8]<=0.0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[12]>2:
				# {"feature": "Education", "instances": 281, "metric_value": 0.4772, "depth": 4}
				if obj[6]>0:
					# {"feature": "Age", "instances": 199, "metric_value": 0.4637, "depth": 5}
					if obj[4]<=4:
						# {"feature": "Occupation", "instances": 174, "metric_value": 0.4818, "depth": 6}
						if obj[7]<=11:
							# {"feature": "Passanger", "instances": 141, "metric_value": 0.4783, "depth": 7}
							if obj[0]>0:
								# {"feature": "Restaurant20to50", "instances": 137, "metric_value": 0.4729, "depth": 8}
								if obj[10]<=2.0:
									# {"feature": "Bar", "instances": 120, "metric_value": 0.4949, "depth": 9}
									if obj[8]>0.0:
										# {"feature": "Gender", "instances": 83, "metric_value": 0.4622, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Time", "instances": 49, "metric_value": 0.463, "depth": 11}
											if obj[1]<=1:
												# {"feature": "Children", "instances": 39, "metric_value": 0.4988, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 28, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 11, "metric_value": 0.4959, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[1]>1:
												# {"feature": "Children", "instances": 10, "metric_value": 0.3, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]>0:
											# {"feature": "Time", "instances": 34, "metric_value": 0.3782, "depth": 11}
											if obj[1]>0:
												# {"feature": "Children", "instances": 28, "metric_value": 0.4365, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 18, "metric_value": 0.4012, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 10, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[1]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[8]<=0.0:
										# {"feature": "Gender", "instances": 37, "metric_value": 0.4702, "depth": 10}
										if obj[3]>0:
											# {"feature": "Time", "instances": 26, "metric_value": 0.4487, "depth": 11}
											if obj[1]>0:
												# {"feature": "Children", "instances": 24, "metric_value": 0.4861, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 12, "metric_value": 0.4861, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]<=0:
													# {"feature": "Direction_same", "instances": 12, "metric_value": 0.4861, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[1]<=0:
												return 'True'
											else: return 'True'
										elif obj[3]<=0:
											# {"feature": "Time", "instances": 11, "metric_value": 0.3636, "depth": 11}
											if obj[1]>0:
												# {"feature": "Children", "instances": 8, "metric_value": 0.5, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[5]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[1]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[10]>2.0:
									# {"feature": "Time", "instances": 17, "metric_value": 0.0882, "depth": 9}
									if obj[1]<=1:
										return 'False'
									elif obj[1]>1:
										# {"feature": "Bar", "instances": 4, "metric_value": 0.0, "depth": 10}
										if obj[8]>1.0:
											return 'True'
										elif obj[8]<=1.0:
											return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'False'
							elif obj[0]<=0:
								return 'True'
							else: return 'True'
						elif obj[7]>11:
							# {"feature": "Restaurant20to50", "instances": 33, "metric_value": 0.3673, "depth": 7}
							if obj[10]<=3.0:
								# {"feature": "Bar", "instances": 29, "metric_value": 0.3291, "depth": 8}
								if obj[8]<=2.0:
									# {"feature": "Time", "instances": 20, "metric_value": 0.2471, "depth": 9}
									if obj[1]>0:
										# {"feature": "Children", "instances": 17, "metric_value": 0.2891, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Gender", "instances": 10, "metric_value": 0.2857, "depth": 11}
											if obj[3]>0:
												# {"feature": "Passanger", "instances": 7, "metric_value": 0.4082, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4082, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]<=0:
												return 'True'
											else: return 'True'
										elif obj[5]>0:
											# {"feature": "Gender", "instances": 7, "metric_value": 0.1905, "depth": 11}
											if obj[3]>0:
												return 'True'
											elif obj[3]<=0:
												# {"feature": "Passanger", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[1]<=0:
										return 'True'
									else: return 'True'
								elif obj[8]>2.0:
									# {"feature": "Time", "instances": 9, "metric_value": 0.3175, "depth": 9}
									if obj[1]>0:
										# {"feature": "Gender", "instances": 7, "metric_value": 0.2857, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Passanger", "instances": 4, "metric_value": 0.5, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Children", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]>0:
											return 'True'
										else: return 'True'
									elif obj[1]<=0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[10]>3.0:
								# {"feature": "Gender", "instances": 4, "metric_value": 0.25, "depth": 8}
								if obj[3]<=0:
									return 'False'
								elif obj[3]>0:
									# {"feature": "Passanger", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Time", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[1]<=1:
											# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Bar", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[8]<=2.0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[4]>4:
						# {"feature": "Occupation", "instances": 25, "metric_value": 0.1467, "depth": 6}
						if obj[7]<=16:
							# {"feature": "Bar", "instances": 24, "metric_value": 0.1417, "depth": 7}
							if obj[8]<=1.0:
								# {"feature": "Restaurant20to50", "instances": 20, "metric_value": 0.0909, "depth": 8}
								if obj[10]>1.0:
									# {"feature": "Gender", "instances": 11, "metric_value": 0.1515, "depth": 9}
									if obj[3]>0:
										# {"feature": "Time", "instances": 6, "metric_value": 0.25, "depth": 10}
										if obj[1]<=1:
											# {"feature": "Passanger", "instances": 4, "metric_value": 0.375, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Children", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[5]<=1:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[1]>1:
											return 'False'
										else: return 'False'
									elif obj[3]<=0:
										return 'False'
									else: return 'False'
								elif obj[10]<=1.0:
									return 'False'
								else: return 'False'
							elif obj[8]>1.0:
								# {"feature": "Children", "instances": 4, "metric_value": 0.0, "depth": 8}
								if obj[5]<=0:
									return 'False'
								elif obj[5]>0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[7]>16:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[6]<=0:
					# {"feature": "Occupation", "instances": 82, "metric_value": 0.4027, "depth": 5}
					if obj[7]>4:
						# {"feature": "Age", "instances": 62, "metric_value": 0.4622, "depth": 6}
						if obj[4]<=6:
							# {"feature": "Restaurant20to50", "instances": 61, "metric_value": 0.4568, "depth": 7}
							if obj[10]<=3.0:
								# {"feature": "Gender", "instances": 60, "metric_value": 0.4568, "depth": 8}
								if obj[3]<=0:
									# {"feature": "Bar", "instances": 35, "metric_value": 0.4038, "depth": 9}
									if obj[8]<=2.0:
										# {"feature": "Time", "instances": 30, "metric_value": 0.3826, "depth": 10}
										if obj[1]>0:
											# {"feature": "Children", "instances": 22, "metric_value": 0.3481, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Passanger", "instances": 15, "metric_value": 0.32, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Direction_same", "instances": 15, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[5]>0:
												# {"feature": "Passanger", "instances": 7, "metric_value": 0.4082, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4082, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[1]<=0:
											# {"feature": "Passanger", "instances": 8, "metric_value": 0.4583, "depth": 11}
											if obj[0]>0:
												# {"feature": "Children", "instances": 6, "metric_value": 0.4, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													return 'True'
												else: return 'True'
											elif obj[0]<=0:
												# {"feature": "Children", "instances": 2, "metric_value": 0.0, "depth": 12}
												if obj[5]>0:
													return 'False'
												elif obj[5]<=0:
													return 'True'
												else: return 'True'
											else: return 'False'
										else: return 'True'
									elif obj[8]>2.0:
										# {"feature": "Passanger", "instances": 5, "metric_value": 0.48, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Time", "instances": 5, "metric_value": 0.48, "depth": 11}
											if obj[1]<=1:
												# {"feature": "Children", "instances": 5, "metric_value": 0.48, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[3]>0:
									# {"feature": "Bar", "instances": 25, "metric_value": 0.4588, "depth": 9}
									if obj[8]<=1.0:
										# {"feature": "Passanger", "instances": 17, "metric_value": 0.4632, "depth": 10}
										if obj[0]>0:
											# {"feature": "Time", "instances": 16, "metric_value": 0.4375, "depth": 11}
											if obj[1]>0:
												# {"feature": "Children", "instances": 14, "metric_value": 0.5, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[1]<=0:
												return 'False'
											else: return 'False'
										elif obj[0]<=0:
											return 'True'
										else: return 'True'
									elif obj[8]>1.0:
										# {"feature": "Children", "instances": 8, "metric_value": 0.3333, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Time", "instances": 6, "metric_value": 0.25, "depth": 11}
											if obj[1]>0:
												# {"feature": "Passanger", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[1]<=0:
												return 'True'
											else: return 'True'
										elif obj[5]>0:
											# {"feature": "Time", "instances": 2, "metric_value": 0.0, "depth": 11}
											if obj[1]<=0:
												return 'False'
											elif obj[1]>0:
												return 'True'
											else: return 'True'
										else: return 'False'
									else: return 'True'
								else: return 'True'
							elif obj[10]>3.0:
								return 'False'
							else: return 'False'
						elif obj[4]>6:
							return 'False'
						else: return 'False'
					elif obj[7]<=4:
						# {"feature": "Time", "instances": 20, "metric_value": 0.1608, "depth": 6}
						if obj[1]<=1:
							# {"feature": "Gender", "instances": 17, "metric_value": 0.0941, "depth": 7}
							if obj[3]>0:
								return 'True'
							elif obj[3]<=0:
								# {"feature": "Bar", "instances": 5, "metric_value": 0.2, "depth": 8}
								if obj[8]<=0.0:
									return 'True'
								elif obj[8]>0.0:
									# {"feature": "Passanger", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Age", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[4]<=4:
											# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0.0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
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
		if obj[8]>0.0:
			# {"feature": "Passanger", "instances": 1286, "metric_value": 0.4891, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Time", "instances": 1095, "metric_value": 0.4916, "depth": 4}
				if obj[1]>0:
					# {"feature": "Restaurant20to50", "instances": 757, "metric_value": 0.4869, "depth": 5}
					if obj[10]<=2.0:
						# {"feature": "Education", "instances": 686, "metric_value": 0.4848, "depth": 6}
						if obj[6]>1:
							# {"feature": "Coffeehouse", "instances": 406, "metric_value": 0.4662, "depth": 7}
							if obj[9]>1.0:
								# {"feature": "Age", "instances": 220, "metric_value": 0.4832, "depth": 8}
								if obj[4]>0:
									# {"feature": "Occupation", "instances": 195, "metric_value": 0.4939, "depth": 9}
									if obj[7]<=17:
										# {"feature": "Gender", "instances": 181, "metric_value": 0.4934, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Children", "instances": 99, "metric_value": 0.4987, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Direction_same", "instances": 59, "metric_value": 0.4891, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 52, "metric_value": 0.4931, "depth": 13}
													if obj[12]>1:
														return 'True'
													elif obj[12]<=1:
														return 'False'
													else: return 'False'
												elif obj[11]>0:
													# {"feature": "Distance", "instances": 7, "metric_value": 0.4048, "depth": 13}
													if obj[12]>1:
														return 'False'
													elif obj[12]<=1:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[5]>0:
												# {"feature": "Distance", "instances": 40, "metric_value": 0.4616, "depth": 12}
												if obj[12]>1:
													# {"feature": "Direction_same", "instances": 31, "metric_value": 0.4854, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[12]<=1:
													# {"feature": "Direction_same", "instances": 9, "metric_value": 0.3333, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]>0:
											# {"feature": "Children", "instances": 82, "metric_value": 0.4728, "depth": 11}
											if obj[5]>0:
												# {"feature": "Distance", "instances": 44, "metric_value": 0.4325, "depth": 12}
												if obj[12]>1:
													# {"feature": "Direction_same", "instances": 33, "metric_value": 0.4761, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												elif obj[12]<=1:
													# {"feature": "Direction_same", "instances": 11, "metric_value": 0.2909, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[5]<=0:
												# {"feature": "Distance", "instances": 38, "metric_value": 0.4773, "depth": 12}
												if obj[12]>1:
													# {"feature": "Direction_same", "instances": 22, "metric_value": 0.4625, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[12]<=1:
													# {"feature": "Direction_same", "instances": 16, "metric_value": 0.4688, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[7]>17:
										# {"feature": "Gender", "instances": 14, "metric_value": 0.3571, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Children", "instances": 10, "metric_value": 0.4167, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 5, "metric_value": 0.4667, "depth": 13}
													if obj[12]>1:
														return 'True'
													elif obj[12]<=1:
														return 'False'
													else: return 'False'
												elif obj[11]>0:
													return 'True'
												else: return 'True'
											elif obj[5]>0:
												# {"feature": "Distance", "instances": 4, "metric_value": 0.25, "depth": 12}
												if obj[12]>1:
													return 'False'
												elif obj[12]<=1:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[3]>0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[4]<=0:
									# {"feature": "Distance", "instances": 25, "metric_value": 0.3284, "depth": 9}
									if obj[12]<=2:
										# {"feature": "Occupation", "instances": 19, "metric_value": 0.4087, "depth": 10}
										if obj[7]>1:
											# {"feature": "Gender", "instances": 17, "metric_value": 0.4373, "depth": 11}
											if obj[3]>0:
												# {"feature": "Children", "instances": 12, "metric_value": 0.4815, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4815, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[3]<=0:
												# {"feature": "Children", "instances": 5, "metric_value": 0.3, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.3333, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												elif obj[5]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[7]<=1:
											return 'False'
										else: return 'False'
									elif obj[12]>2:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[9]<=1.0:
								# {"feature": "Age", "instances": 186, "metric_value": 0.4154, "depth": 8}
								if obj[4]<=4:
									# {"feature": "Occupation", "instances": 144, "metric_value": 0.4306, "depth": 9}
									if obj[7]>5:
										# {"feature": "Gender", "instances": 109, "metric_value": 0.4056, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Distance", "instances": 59, "metric_value": 0.4162, "depth": 11}
											if obj[12]>1:
												# {"feature": "Children", "instances": 36, "metric_value": 0.4954, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 24, "metric_value": 0.4921, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 12, "metric_value": 0.4545, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[12]<=1:
												# {"feature": "Children", "instances": 23, "metric_value": 0.2705, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 18, "metric_value": 0.3259, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												elif obj[5]>0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[3]>0:
											# {"feature": "Distance", "instances": 50, "metric_value": 0.3087, "depth": 11}
											if obj[12]<=1:
												# {"feature": "Direction_same", "instances": 26, "metric_value": 0.4185, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Children", "instances": 25, "metric_value": 0.432, "depth": 13}
													if obj[5]<=0:
														return 'False'
													elif obj[5]>0:
														return 'False'
													else: return 'False'
												elif obj[11]>0:
													return 'True'
												else: return 'True'
											elif obj[12]>1:
												# {"feature": "Children", "instances": 24, "metric_value": 0.1296, "depth": 12}
												if obj[5]<=0:
													return 'False'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 9, "metric_value": 0.3333, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[7]<=5:
										# {"feature": "Direction_same", "instances": 35, "metric_value": 0.4484, "depth": 10}
										if obj[11]<=0:
											# {"feature": "Gender", "instances": 31, "metric_value": 0.4469, "depth": 11}
											if obj[3]>0:
												# {"feature": "Children", "instances": 20, "metric_value": 0.3725, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Distance", "instances": 17, "metric_value": 0.3494, "depth": 13}
													if obj[12]>1:
														return 'True'
													elif obj[12]<=1:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Distance", "instances": 3, "metric_value": 0.3333, "depth": 13}
													if obj[12]<=1:
														return 'True'
													elif obj[12]>1:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[3]<=0:
												# {"feature": "Children", "instances": 11, "metric_value": 0.4545, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Distance", "instances": 10, "metric_value": 0.5, "depth": 13}
													if obj[12]>1:
														return 'True'
													elif obj[12]<=1:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[11]>0:
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
										if obj[7]<=6:
											return 'False'
										elif obj[7]>6:
											# {"feature": "Distance", "instances": 6, "metric_value": 0.2667, "depth": 11}
											if obj[12]>1:
												# {"feature": "Children", "instances": 5, "metric_value": 0.32, "depth": 12}
												if obj[5]<=1:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[12]<=1:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[3]<=0:
										# {"feature": "Children", "instances": 17, "metric_value": 0.2824, "depth": 10}
										if obj[5]>0:
											# {"feature": "Distance", "instances": 15, "metric_value": 0.2667, "depth": 11}
											if obj[12]>1:
												# {"feature": "Direction_same", "instances": 9, "metric_value": 0.3333, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Occupation", "instances": 8, "metric_value": 0.3333, "depth": 13}
													if obj[7]<=12:
														return 'False'
													elif obj[7]>12:
														return 'False'
													else: return 'False'
												elif obj[11]>0:
													return 'True'
												else: return 'True'
											elif obj[12]<=1:
												return 'False'
											else: return 'False'
										elif obj[5]<=0:
											return 'True'
										else: return 'True'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[6]<=1:
							# {"feature": "Children", "instances": 280, "metric_value": 0.4923, "depth": 7}
							if obj[5]<=0:
								# {"feature": "Coffeehouse", "instances": 194, "metric_value": 0.4861, "depth": 8}
								if obj[9]<=3.0:
									# {"feature": "Age", "instances": 173, "metric_value": 0.48, "depth": 9}
									if obj[4]>0:
										# {"feature": "Distance", "instances": 122, "metric_value": 0.4696, "depth": 10}
										if obj[12]>1:
											# {"feature": "Occupation", "instances": 77, "metric_value": 0.4454, "depth": 11}
											if obj[7]>1:
												# {"feature": "Gender", "instances": 74, "metric_value": 0.4599, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 48, "metric_value": 0.4783, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 26, "metric_value": 0.4248, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[7]<=1:
												return 'True'
											else: return 'True'
										elif obj[12]<=1:
											# {"feature": "Occupation", "instances": 45, "metric_value": 0.4866, "depth": 11}
											if obj[7]<=10:
												# {"feature": "Direction_same", "instances": 32, "metric_value": 0.4684, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Gender", "instances": 29, "metric_value": 0.4487, "depth": 13}
													if obj[3]<=0:
														return 'True'
													elif obj[3]>0:
														return 'True'
													else: return 'True'
												elif obj[11]>0:
													# {"feature": "Gender", "instances": 3, "metric_value": 0.3333, "depth": 13}
													if obj[3]<=0:
														return 'True'
													elif obj[3]>0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[7]>10:
												# {"feature": "Gender", "instances": 13, "metric_value": 0.4872, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 10, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[4]<=0:
										# {"feature": "Occupation", "instances": 51, "metric_value": 0.4575, "depth": 10}
										if obj[7]>0:
											# {"feature": "Distance", "instances": 48, "metric_value": 0.4444, "depth": 11}
											if obj[12]<=2:
												# {"feature": "Gender", "instances": 36, "metric_value": 0.4931, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 24, "metric_value": 0.4962, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 12, "metric_value": 0.4815, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[12]>2:
												# {"feature": "Gender", "instances": 12, "metric_value": 0.2, "depth": 12}
												if obj[3]>0:
													return 'False'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[7]<=0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[9]>3.0:
									# {"feature": "Distance", "instances": 21, "metric_value": 0.3627, "depth": 9}
									if obj[12]<=2:
										# {"feature": "Age", "instances": 17, "metric_value": 0.3137, "depth": 10}
										if obj[4]<=4:
											# {"feature": "Direction_same", "instances": 12, "metric_value": 0.4, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Occupation", "instances": 10, "metric_value": 0.4667, "depth": 12}
												if obj[7]>5:
													# {"feature": "Gender", "instances": 6, "metric_value": 0.4444, "depth": 13}
													if obj[3]<=1:
														return 'False'
													else: return 'False'
												elif obj[7]<=5:
													# {"feature": "Gender", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[3]<=0:
														return 'False'
													elif obj[3]>0:
														return 'True'
													else: return 'True'
												else: return 'False'
											elif obj[11]>0:
												return 'False'
											else: return 'False'
										elif obj[4]>4:
											return 'False'
										else: return 'False'
									elif obj[12]>2:
										# {"feature": "Occupation", "instances": 4, "metric_value": 0.0, "depth": 10}
										if obj[7]>1:
											return 'True'
										elif obj[7]<=1:
											return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'False'
							elif obj[5]>0:
								# {"feature": "Distance", "instances": 86, "metric_value": 0.4299, "depth": 8}
								if obj[12]<=2:
									# {"feature": "Age", "instances": 60, "metric_value": 0.4074, "depth": 9}
									if obj[4]<=4:
										# {"feature": "Gender", "instances": 51, "metric_value": 0.4277, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Occupation", "instances": 26, "metric_value": 0.4493, "depth": 11}
											if obj[7]>2:
												# {"feature": "Coffeehouse", "instances": 22, "metric_value": 0.4591, "depth": 12}
												if obj[9]>0.0:
													# {"feature": "Direction_same", "instances": 20, "metric_value": 0.4549, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												elif obj[9]<=0.0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[7]<=2:
												# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.3333, "depth": 12}
												if obj[9]>1.0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.3333, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[9]<=1.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]>0:
											# {"feature": "Occupation", "instances": 25, "metric_value": 0.336, "depth": 11}
											if obj[7]>3:
												# {"feature": "Direction_same", "instances": 20, "metric_value": 0.4133, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Coffeehouse", "instances": 15, "metric_value": 0.4444, "depth": 13}
													if obj[9]>1.0:
														return 'False'
													elif obj[9]<=1.0:
														return 'False'
													else: return 'False'
												elif obj[11]>0:
													# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.2667, "depth": 13}
													if obj[9]>1.0:
														return 'False'
													elif obj[9]<=1.0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[7]<=3:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[4]>4:
										# {"feature": "Occupation", "instances": 9, "metric_value": 0.1481, "depth": 10}
										if obj[7]<=15:
											return 'False'
										elif obj[7]>15:
											# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[3]<=1:
												# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[9]<=0.0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[12]>2:
									# {"feature": "Age", "instances": 26, "metric_value": 0.3956, "depth": 9}
									if obj[4]<=4:
										# {"feature": "Occupation", "instances": 21, "metric_value": 0.4444, "depth": 10}
										if obj[7]<=12:
											# {"feature": "Gender", "instances": 15, "metric_value": 0.4074, "depth": 11}
											if obj[3]>0:
												# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.3333, "depth": 12}
												if obj[9]>1.0:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.2778, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[9]<=1.0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.4, "depth": 12}
												if obj[9]<=1.0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[9]>1.0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[7]>12:
											# {"feature": "Gender", "instances": 6, "metric_value": 0.3333, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.3333, "depth": 12}
												if obj[9]>1.0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[9]<=1.0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[4]>4:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'False'
					elif obj[10]>2.0:
						# {"feature": "Occupation", "instances": 71, "metric_value": 0.4231, "depth": 6}
						if obj[7]<=14:
							# {"feature": "Gender", "instances": 59, "metric_value": 0.3956, "depth": 7}
							if obj[3]<=0:
								# {"feature": "Education", "instances": 33, "metric_value": 0.2754, "depth": 8}
								if obj[6]<=2:
									# {"feature": "Distance", "instances": 18, "metric_value": 0.0833, "depth": 9}
									if obj[12]<=2:
										return 'True'
									elif obj[12]>2:
										# {"feature": "Age", "instances": 4, "metric_value": 0.25, "depth": 10}
										if obj[4]<=2:
											return 'True'
										elif obj[4]>2:
											# {"feature": "Coffeehouse", "instances": 2, "metric_value": 0.0, "depth": 11}
											if obj[9]<=2.0:
												return 'True'
											elif obj[9]>2.0:
												return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'True'
								elif obj[6]>2:
									# {"feature": "Direction_same", "instances": 15, "metric_value": 0.3692, "depth": 9}
									if obj[11]<=0:
										# {"feature": "Age", "instances": 13, "metric_value": 0.2521, "depth": 10}
										if obj[4]>0:
											# {"feature": "Distance", "instances": 9, "metric_value": 0.1667, "depth": 11}
											if obj[12]>1:
												return 'True'
											elif obj[12]<=1:
												# {"feature": "Children", "instances": 4, "metric_value": 0.3333, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.3333, "depth": 13}
													if obj[9]>1.0:
														return 'True'
													elif obj[9]<=1.0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[4]<=0:
											# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.0, "depth": 11}
											if obj[9]<=2.0:
												return 'False'
											elif obj[9]>2.0:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[11]>0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[3]>0:
								# {"feature": "Education", "instances": 26, "metric_value": 0.3846, "depth": 8}
								if obj[6]<=3:
									# {"feature": "Age", "instances": 20, "metric_value": 0.4545, "depth": 9}
									if obj[4]>2:
										# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.3117, "depth": 10}
										if obj[9]<=2.0:
											# {"feature": "Distance", "instances": 7, "metric_value": 0.4048, "depth": 11}
											if obj[12]<=1:
												# {"feature": "Children", "instances": 4, "metric_value": 0.3333, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.3333, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													return 'True'
												else: return 'True'
											elif obj[12]>1:
												# {"feature": "Children", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[9]>2.0:
											return 'False'
										else: return 'False'
									elif obj[4]<=2:
										# {"feature": "Children", "instances": 9, "metric_value": 0.3333, "depth": 10}
										if obj[5]>0:
											# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.4, "depth": 11}
											if obj[9]<=3.0:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.4, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 4, "metric_value": 0.3333, "depth": 13}
													if obj[12]<=2:
														return 'True'
													elif obj[12]>2:
														return 'False'
													else: return 'False'
												elif obj[11]>0:
													return 'False'
												else: return 'False'
											elif obj[9]>3.0:
												return 'True'
											else: return 'True'
										elif obj[5]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[6]>3:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[7]>14:
							# {"feature": "Education", "instances": 12, "metric_value": 0.3125, "depth": 7}
							if obj[6]<=2:
								# {"feature": "Age", "instances": 8, "metric_value": 0.1875, "depth": 8}
								if obj[4]<=0:
									# {"feature": "Distance", "instances": 4, "metric_value": 0.0, "depth": 9}
									if obj[12]<=2:
										return 'False'
									elif obj[12]>2:
										return 'True'
									else: return 'True'
								elif obj[4]>0:
									return 'True'
								else: return 'True'
							elif obj[6]>2:
								return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[1]<=0:
					# {"feature": "Distance", "instances": 338, "metric_value": 0.4678, "depth": 5}
					if obj[12]>1:
						# {"feature": "Direction_same", "instances": 182, "metric_value": 0.485, "depth": 6}
						if obj[11]<=0:
							# {"feature": "Age", "instances": 171, "metric_value": 0.4792, "depth": 7}
							if obj[4]>1:
								# {"feature": "Children", "instances": 111, "metric_value": 0.4836, "depth": 8}
								if obj[5]<=0:
									# {"feature": "Restaurant20to50", "instances": 67, "metric_value": 0.4748, "depth": 9}
									if obj[10]>0.0:
										# {"feature": "Coffeehouse", "instances": 59, "metric_value": 0.4643, "depth": 10}
										if obj[9]<=2.0:
											# {"feature": "Occupation", "instances": 38, "metric_value": 0.3529, "depth": 11}
											if obj[7]>5:
												# {"feature": "Education", "instances": 26, "metric_value": 0.2585, "depth": 12}
												if obj[6]<=3:
													# {"feature": "Gender", "instances": 25, "metric_value": 0.2686, "depth": 13}
													if obj[3]<=0:
														return 'True'
													elif obj[3]>0:
														return 'True'
													else: return 'True'
												elif obj[6]>3:
													return 'False'
												else: return 'False'
											elif obj[7]<=5:
												# {"feature": "Education", "instances": 12, "metric_value": 0.3636, "depth": 12}
												if obj[6]<=2:
													# {"feature": "Gender", "instances": 11, "metric_value": 0.3697, "depth": 13}
													if obj[3]>0:
														return 'False'
													elif obj[3]<=0:
														return 'False'
													else: return 'False'
												elif obj[6]>2:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[9]>2.0:
											# {"feature": "Occupation", "instances": 21, "metric_value": 0.4211, "depth": 11}
											if obj[7]>1:
												# {"feature": "Education", "instances": 19, "metric_value": 0.4561, "depth": 12}
												if obj[6]<=2:
													# {"feature": "Gender", "instances": 15, "metric_value": 0.4074, "depth": 13}
													if obj[3]>0:
														return 'False'
													elif obj[3]<=0:
														return 'False'
													else: return 'False'
												elif obj[6]>2:
													# {"feature": "Gender", "instances": 4, "metric_value": 0.3333, "depth": 13}
													if obj[3]>0:
														return 'False'
													elif obj[3]<=0:
														return 'True'
													else: return 'True'
												else: return 'False'
											elif obj[7]<=1:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[10]<=0.0:
										# {"feature": "Education", "instances": 8, "metric_value": 0.2143, "depth": 10}
										if obj[6]<=2:
											# {"feature": "Gender", "instances": 7, "metric_value": 0.1429, "depth": 11}
											if obj[3]<=0:
												return 'False'
											elif obj[3]>0:
												# {"feature": "Occupation", "instances": 2, "metric_value": 0.0, "depth": 12}
												if obj[7]<=6:
													return 'True'
												elif obj[7]>6:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[6]>2:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[5]>0:
									# {"feature": "Coffeehouse", "instances": 44, "metric_value": 0.4299, "depth": 9}
									if obj[9]>0.0:
										# {"feature": "Occupation", "instances": 34, "metric_value": 0.3975, "depth": 10}
										if obj[7]>7:
											# {"feature": "Gender", "instances": 19, "metric_value": 0.3218, "depth": 11}
											if obj[3]>0:
												# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.3377, "depth": 12}
												if obj[10]<=1.0:
													# {"feature": "Education", "instances": 7, "metric_value": 0.2143, "depth": 13}
													if obj[6]>1:
														return 'False'
													elif obj[6]<=1:
														return 'False'
													else: return 'False'
												elif obj[10]>1.0:
													# {"feature": "Education", "instances": 4, "metric_value": 0.0, "depth": 13}
													if obj[6]>2:
														return 'True'
													elif obj[6]<=2:
														return 'False'
													else: return 'False'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.125, "depth": 12}
												if obj[10]>0.0:
													return 'False'
												elif obj[10]<=0.0:
													# {"feature": "Education", "instances": 2, "metric_value": 0.0, "depth": 13}
													if obj[6]<=0:
														return 'True'
													elif obj[6]>0:
														return 'False'
													else: return 'False'
												else: return 'True'
											else: return 'False'
										elif obj[7]<=7:
											# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.4444, "depth": 11}
											if obj[10]>0.0:
												# {"feature": "Education", "instances": 12, "metric_value": 0.4167, "depth": 12}
												if obj[6]<=2:
													# {"feature": "Gender", "instances": 8, "metric_value": 0.3667, "depth": 13}
													if obj[3]>0:
														return 'False'
													elif obj[3]<=0:
														return 'False'
													else: return 'False'
												elif obj[6]>2:
													# {"feature": "Gender", "instances": 4, "metric_value": 0.3333, "depth": 13}
													if obj[3]>0:
														return 'True'
													elif obj[3]<=0:
														return 'False'
													else: return 'False'
												else: return 'True'
											elif obj[10]<=0.0:
												# {"feature": "Gender", "instances": 3, "metric_value": 0.3333, "depth": 12}
												if obj[3]>0:
													# {"feature": "Education", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[6]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[9]<=0.0:
										# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.2667, "depth": 10}
										if obj[10]<=1.0:
											# {"feature": "Gender", "instances": 6, "metric_value": 0.2222, "depth": 11}
											if obj[3]>0:
												return 'False'
											elif obj[3]<=0:
												# {"feature": "Education", "instances": 3, "metric_value": 0.3333, "depth": 12}
												if obj[6]>0:
													# {"feature": "Occupation", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[7]<=6:
														return 'True'
													else: return 'True'
												elif obj[6]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[10]>1.0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[4]<=1:
								# {"feature": "Occupation", "instances": 60, "metric_value": 0.3907, "depth": 8}
								if obj[7]>3:
									# {"feature": "Children", "instances": 50, "metric_value": 0.3321, "depth": 9}
									if obj[5]<=0:
										# {"feature": "Coffeehouse", "instances": 31, "metric_value": 0.4227, "depth": 10}
										if obj[9]<=3.0:
											# {"feature": "Restaurant20to50", "instances": 29, "metric_value": 0.4212, "depth": 11}
											if obj[10]<=2.0:
												# {"feature": "Education", "instances": 28, "metric_value": 0.4203, "depth": 12}
												if obj[6]<=3:
													# {"feature": "Gender", "instances": 26, "metric_value": 0.4448, "depth": 13}
													if obj[3]>0:
														return 'True'
													elif obj[3]<=0:
														return 'True'
													else: return 'True'
												elif obj[6]>3:
													return 'True'
												else: return 'True'
											elif obj[10]>2.0:
												return 'False'
											else: return 'False'
										elif obj[9]>3.0:
											return 'False'
										else: return 'False'
									elif obj[5]>0:
										# {"feature": "Coffeehouse", "instances": 19, "metric_value": 0.0842, "depth": 10}
										if obj[9]<=2.0:
											return 'True'
										elif obj[9]>2.0:
											# {"feature": "Education", "instances": 5, "metric_value": 0.0, "depth": 11}
											if obj[6]>1:
												return 'True'
											elif obj[6]<=1:
												return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'True'
								elif obj[7]<=3:
									# {"feature": "Gender", "instances": 10, "metric_value": 0.175, "depth": 9}
									if obj[3]>0:
										# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.1875, "depth": 10}
										if obj[9]>1.0:
											return 'False'
										elif obj[9]<=1.0:
											# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.25, "depth": 11}
											if obj[10]>1.0:
												# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Education", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[6]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[10]<=1.0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[3]<=0:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'True'
						elif obj[11]>0:
							# {"feature": "Occupation", "instances": 11, "metric_value": 0.2424, "depth": 7}
							if obj[7]<=6:
								# {"feature": "Age", "instances": 6, "metric_value": 0.3333, "depth": 8}
								if obj[4]>0:
									# {"feature": "Gender", "instances": 4, "metric_value": 0.3333, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Education", "instances": 3, "metric_value": 0.0, "depth": 10}
										if obj[6]>0:
											return 'False'
										elif obj[6]<=0:
											return 'True'
										else: return 'True'
									elif obj[3]>0:
										return 'True'
									else: return 'True'
								elif obj[4]<=0:
									return 'False'
								else: return 'False'
							elif obj[7]>6:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[12]<=1:
						# {"feature": "Direction_same", "instances": 156, "metric_value": 0.4105, "depth": 6}
						if obj[11]>0:
							# {"feature": "Restaurant20to50", "instances": 146, "metric_value": 0.3926, "depth": 7}
							if obj[10]<=1.0:
								# {"feature": "Education", "instances": 92, "metric_value": 0.4484, "depth": 8}
								if obj[6]<=3:
									# {"feature": "Age", "instances": 88, "metric_value": 0.4588, "depth": 9}
									if obj[4]<=6:
										# {"feature": "Gender", "instances": 85, "metric_value": 0.4617, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Occupation", "instances": 50, "metric_value": 0.425, "depth": 11}
											if obj[7]>2.9388214248136357:
												# {"feature": "Coffeehouse", "instances": 43, "metric_value": 0.4485, "depth": 12}
												if obj[9]>-1.0:
													# {"feature": "Children", "instances": 42, "metric_value": 0.4585, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												elif obj[9]<=-1.0:
													return 'True'
												else: return 'True'
											elif obj[7]<=2.9388214248136357:
												# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.2143, "depth": 12}
												if obj[9]>1.0:
													# {"feature": "Children", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[5]<=0:
														return 'True'
													else: return 'True'
												elif obj[9]<=1.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]>0:
											# {"feature": "Children", "instances": 35, "metric_value": 0.4504, "depth": 11}
											if obj[5]>0:
												# {"feature": "Occupation", "instances": 18, "metric_value": 0.4167, "depth": 12}
												if obj[7]>4:
													# {"feature": "Coffeehouse", "instances": 12, "metric_value": 0.3125, "depth": 13}
													if obj[9]<=2.0:
														return 'True'
													elif obj[9]>2.0:
														return 'True'
													else: return 'True'
												elif obj[7]<=4:
													# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.4, "depth": 13}
													if obj[9]>0.0:
														return 'False'
													elif obj[9]<=0.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[5]<=0:
												# {"feature": "Coffeehouse", "instances": 17, "metric_value": 0.4044, "depth": 12}
												if obj[9]<=3.0:
													# {"feature": "Occupation", "instances": 16, "metric_value": 0.3846, "depth": 13}
													if obj[7]<=7:
														return 'False'
													elif obj[7]>7:
														return 'False'
													else: return 'False'
												elif obj[9]>3.0:
													return 'True'
												else: return 'True'
											else: return 'False'
										else: return 'True'
									elif obj[4]>6:
										return 'True'
									else: return 'True'
								elif obj[6]>3:
									return 'True'
								else: return 'True'
							elif obj[10]>1.0:
								# {"feature": "Education", "instances": 54, "metric_value": 0.2516, "depth": 8}
								if obj[6]<=4:
									# {"feature": "Occupation", "instances": 53, "metric_value": 0.2478, "depth": 9}
									if obj[7]<=20:
										# {"feature": "Age", "instances": 47, "metric_value": 0.2138, "depth": 10}
										if obj[4]<=2:
											# {"feature": "Gender", "instances": 27, "metric_value": 0.28, "depth": 11}
											if obj[3]>0:
												# {"feature": "Coffeehouse", "instances": 14, "metric_value": 0.3297, "depth": 12}
												if obj[9]<=3.0:
													# {"feature": "Children", "instances": 13, "metric_value": 0.2906, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'False'
													else: return 'False'
												elif obj[9]>3.0:
													return 'False'
												else: return 'False'
											elif obj[3]<=0:
												# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.1319, "depth": 12}
												if obj[9]<=2.0:
													# {"feature": "Children", "instances": 7, "metric_value": 0.2143, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												elif obj[9]>2.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[4]>2:
											# {"feature": "Gender", "instances": 20, "metric_value": 0.09, "depth": 11}
											if obj[3]>0:
												return 'True'
											elif obj[3]<=0:
												# {"feature": "Children", "instances": 10, "metric_value": 0.1667, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.2222, "depth": 13}
													if obj[9]<=1.0:
														return 'True'
													elif obj[9]>1.0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[7]>20:
										# {"feature": "Age", "instances": 6, "metric_value": 0.2222, "depth": 10}
										if obj[4]<=2:
											return 'True'
										elif obj[4]>2:
											# {"feature": "Children", "instances": 3, "metric_value": 0.0, "depth": 11}
											if obj[5]>0:
												return 'False'
											elif obj[5]<=0:
												return 'True'
											else: return 'True'
										else: return 'False'
									else: return 'True'
								elif obj[6]>4:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[11]<=0:
							# {"feature": "Age", "instances": 10, "metric_value": 0.3, "depth": 7}
							if obj[4]>0:
								# {"feature": "Gender", "instances": 6, "metric_value": 0.25, "depth": 8}
								if obj[3]<=0:
									# {"feature": "Occupation", "instances": 4, "metric_value": 0.0, "depth": 9}
									if obj[7]<=9:
										return 'True'
									elif obj[7]>9:
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
					if obj[7]<=7.54054054054054:
						# {"feature": "Age", "instances": 92, "metric_value": 0.3936, "depth": 6}
						if obj[4]<=5:
							# {"feature": "Coffeehouse", "instances": 81, "metric_value": 0.3926, "depth": 7}
							if obj[9]>1.0:
								# {"feature": "Education", "instances": 47, "metric_value": 0.2993, "depth": 8}
								if obj[6]<=2:
									# {"feature": "Restaurant20to50", "instances": 36, "metric_value": 0.2239, "depth": 9}
									if obj[10]>0.0:
										# {"feature": "Children", "instances": 34, "metric_value": 0.1986, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Distance", "instances": 31, "metric_value": 0.1743, "depth": 11}
											if obj[12]>1:
												# {"feature": "Gender", "instances": 23, "metric_value": 0.1507, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 15, "metric_value": 0.2311, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											elif obj[12]<=1:
												# {"feature": "Gender", "instances": 8, "metric_value": 0.125, "depth": 12}
												if obj[3]<=0:
													return 'True'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[5]>0:
											# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[3]<=1:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[12]<=2:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[10]<=0.0:
										# {"feature": "Gender", "instances": 2, "metric_value": 0.0, "depth": 10}
										if obj[3]>0:
											return 'True'
										elif obj[3]<=0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[6]>2:
									# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.3636, "depth": 9}
									if obj[10]<=3.0:
										# {"feature": "Gender", "instances": 9, "metric_value": 0.4, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Children", "instances": 5, "metric_value": 0.2, "depth": 11}
											if obj[5]>0:
												return 'True'
											elif obj[5]<=0:
												# {"feature": "Distance", "instances": 2, "metric_value": 0.0, "depth": 12}
												if obj[12]<=1:
													return 'True'
												elif obj[12]>1:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[3]>0:
											# {"feature": "Children", "instances": 4, "metric_value": 0.5, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[12]<=2:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[5]>0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[12]<=2:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[10]>3.0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[9]<=1.0:
								# {"feature": "Education", "instances": 34, "metric_value": 0.3249, "depth": 8}
								if obj[6]>0:
									# {"feature": "Restaurant20to50", "instances": 22, "metric_value": 0.2597, "depth": 9}
									if obj[10]<=1.0:
										# {"feature": "Children", "instances": 14, "metric_value": 0.3929, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Gender", "instances": 12, "metric_value": 0.3125, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Distance", "instances": 8, "metric_value": 0.3571, "depth": 12}
												if obj[12]>1:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4082, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[12]<=1:
													return 'False'
												else: return 'False'
											elif obj[3]>0:
												return 'True'
											else: return 'True'
										elif obj[5]>0:
											# {"feature": "Gender", "instances": 2, "metric_value": 0.0, "depth": 11}
											if obj[3]>0:
												return 'False'
											elif obj[3]<=0:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[10]>1.0:
										return 'True'
									else: return 'True'
								elif obj[6]<=0:
									# {"feature": "Distance", "instances": 12, "metric_value": 0.3333, "depth": 9}
									if obj[12]>1:
										# {"feature": "Gender", "instances": 9, "metric_value": 0.3333, "depth": 10}
										if obj[3]>0:
											# {"feature": "Children", "instances": 6, "metric_value": 0.25, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[10]<=1.0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[5]>0:
												return 'False'
											else: return 'False'
										elif obj[3]<=0:
											# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.0, "depth": 11}
											if obj[10]>0.0:
												return 'True'
											elif obj[10]<=0.0:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[12]<=1:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[4]>5:
							# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.1818, "depth": 7}
							if obj[10]<=2.0:
								return 'False'
							elif obj[10]>2.0:
								# {"feature": "Gender", "instances": 4, "metric_value": 0.0, "depth": 8}
								if obj[3]>0:
									return 'True'
								elif obj[3]<=0:
									return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'False'
					elif obj[7]>7.54054054054054:
						# {"feature": "Coffeehouse", "instances": 56, "metric_value": 0.1676, "depth": 6}
						if obj[9]<=3.0:
							# {"feature": "Gender", "instances": 52, "metric_value": 0.1281, "depth": 7}
							if obj[3]<=0:
								# {"feature": "Age", "instances": 38, "metric_value": 0.0491, "depth": 8}
								if obj[4]>1:
									return 'True'
								elif obj[4]<=1:
									# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.1111, "depth": 9}
									if obj[10]<=1.0:
										return 'True'
									elif obj[10]>1.0:
										# {"feature": "Education", "instances": 6, "metric_value": 0.1667, "depth": 10}
										if obj[6]<=1:
											return 'True'
										elif obj[6]>1:
											# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[12]<=2:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'True'
							elif obj[3]>0:
								# {"feature": "Age", "instances": 14, "metric_value": 0.131, "depth": 8}
								if obj[4]>0:
									# {"feature": "Children", "instances": 12, "metric_value": 0.1333, "depth": 9}
									if obj[5]<=0:
										return 'True'
									elif obj[5]>0:
										# {"feature": "Education", "instances": 5, "metric_value": 0.2667, "depth": 10}
										if obj[6]<=1:
											# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.3333, "depth": 11}
											if obj[10]>0.0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[12]<=2:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[10]<=0.0:
												return 'True'
											else: return 'True'
										elif obj[6]>1:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[4]<=0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[9]>3.0:
							# {"feature": "Gender", "instances": 4, "metric_value": 0.3333, "depth": 7}
							if obj[3]<=0:
								# {"feature": "Education", "instances": 3, "metric_value": 0.0, "depth": 8}
								if obj[6]<=3:
									return 'True'
								elif obj[6]>3:
									return 'False'
								else: return 'False'
							elif obj[3]>0:
								return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[1]<=2:
					# {"feature": "Occupation", "instances": 43, "metric_value": 0.4394, "depth": 5}
					if obj[7]<=12:
						# {"feature": "Restaurant20to50", "instances": 35, "metric_value": 0.4554, "depth": 6}
						if obj[10]>0.0:
							# {"feature": "Education", "instances": 32, "metric_value": 0.4453, "depth": 7}
							if obj[6]>1:
								# {"feature": "Coffeehouse", "instances": 24, "metric_value": 0.4398, "depth": 8}
								if obj[9]>1.0:
									# {"feature": "Children", "instances": 18, "metric_value": 0.4691, "depth": 9}
									if obj[5]<=0:
										# {"feature": "Age", "instances": 9, "metric_value": 0.4167, "depth": 10}
										if obj[4]<=4:
											# {"feature": "Gender", "instances": 8, "metric_value": 0.4667, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[12]<=2:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[12]<=2:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[4]>4:
											return 'False'
										else: return 'False'
									elif obj[5]>0:
										# {"feature": "Age", "instances": 9, "metric_value": 0.4167, "depth": 10}
										if obj[4]>1:
											# {"feature": "Gender", "instances": 8, "metric_value": 0.4583, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4444, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 6, "metric_value": 0.4444, "depth": 13}
													if obj[12]<=2:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[12]<=2:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[4]<=1:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[9]<=1.0:
									# {"feature": "Age", "instances": 6, "metric_value": 0.2222, "depth": 9}
									if obj[4]<=2:
										return 'False'
									elif obj[4]>2:
										# {"feature": "Children", "instances": 3, "metric_value": 0.3333, "depth": 10}
										if obj[5]<=0:
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
										elif obj[5]>0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[6]<=1:
								# {"feature": "Age", "instances": 8, "metric_value": 0.25, "depth": 8}
								if obj[4]<=2:
									# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.3333, "depth": 9}
									if obj[9]<=2.0:
										# {"feature": "Children", "instances": 3, "metric_value": 0.3333, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[3]<=1:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[12]<=2:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[5]>0:
											return 'True'
										else: return 'True'
									elif obj[9]>2.0:
										return 'False'
									else: return 'False'
								elif obj[4]>2:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[10]<=0.0:
							return 'False'
						else: return 'False'
					elif obj[7]>12:
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
		elif obj[8]<=0.0:
			# {"feature": "Children", "instances": 975, "metric_value": 0.3895, "depth": 3}
			if obj[5]>0:
				# {"feature": "Distance", "instances": 529, "metric_value": 0.3323, "depth": 4}
				if obj[12]<=2:
					# {"feature": "Time", "instances": 433, "metric_value": 0.3599, "depth": 5}
					if obj[1]<=3:
						# {"feature": "Restaurant20to50", "instances": 368, "metric_value": 0.3955, "depth": 6}
						if obj[10]>0.0:
							# {"feature": "Coffeehouse", "instances": 301, "metric_value": 0.4179, "depth": 7}
							if obj[9]<=2.0:
								# {"feature": "Age", "instances": 235, "metric_value": 0.4457, "depth": 8}
								if obj[4]<=4:
									# {"feature": "Occupation", "instances": 189, "metric_value": 0.4308, "depth": 9}
									if obj[7]<=12:
										# {"feature": "Passanger", "instances": 170, "metric_value": 0.4383, "depth": 10}
										if obj[0]<=2:
											# {"feature": "Education", "instances": 144, "metric_value": 0.4493, "depth": 11}
											if obj[6]>1:
												# {"feature": "Gender", "instances": 80, "metric_value": 0.4659, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 48, "metric_value": 0.4404, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 32, "metric_value": 0.498, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[6]<=1:
												# {"feature": "Gender", "instances": 64, "metric_value": 0.4011, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 49, "metric_value": 0.4524, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 15, "metric_value": 0.2133, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[0]>2:
											# {"feature": "Education", "instances": 26, "metric_value": 0.3291, "depth": 11}
											if obj[6]>0:
												# {"feature": "Gender", "instances": 15, "metric_value": 0.2286, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 14, "metric_value": 0.2449, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]<=0:
													return 'False'
												else: return 'False'
											elif obj[6]<=0:
												# {"feature": "Gender", "instances": 11, "metric_value": 0.4416, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4082, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'False'
										else: return 'False'
									elif obj[7]>12:
										# {"feature": "Passanger", "instances": 19, "metric_value": 0.1772, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Education", "instances": 15, "metric_value": 0.1143, "depth": 11}
											if obj[6]>1:
												return 'False'
											elif obj[6]<=1:
												# {"feature": "Direction_same", "instances": 7, "metric_value": 0.2143, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Gender", "instances": 4, "metric_value": 0.3333, "depth": 13}
													if obj[3]>0:
														return 'False'
													elif obj[3]<=0:
														return 'False'
													else: return 'False'
												elif obj[11]>0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[0]>1:
											# {"feature": "Gender", "instances": 4, "metric_value": 0.25, "depth": 11}
											if obj[3]>0:
												return 'True'
											elif obj[3]<=0:
												# {"feature": "Education", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[6]<=1:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[4]>4:
									# {"feature": "Occupation", "instances": 46, "metric_value": 0.4597, "depth": 9}
									if obj[7]>1:
										# {"feature": "Passanger", "instances": 36, "metric_value": 0.4746, "depth": 10}
										if obj[0]<=2:
											# {"feature": "Education", "instances": 31, "metric_value": 0.4856, "depth": 11}
											if obj[6]>0:
												# {"feature": "Gender", "instances": 23, "metric_value": 0.4752, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 16, "metric_value": 0.4295, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4857, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[6]<=0:
												# {"feature": "Gender", "instances": 8, "metric_value": 0.4286, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4857, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[0]>2:
											# {"feature": "Gender", "instances": 5, "metric_value": 0.2667, "depth": 11}
											if obj[3]>0:
												# {"feature": "Education", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[6]<=0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[7]<=1:
										# {"feature": "Passanger", "instances": 10, "metric_value": 0.24, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Direction_same", "instances": 5, "metric_value": 0.0, "depth": 11}
											if obj[11]>0:
												return 'False'
											elif obj[11]<=0:
												return 'True'
											else: return 'True'
										elif obj[0]>1:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[9]>2.0:
								# {"feature": "Education", "instances": 66, "metric_value": 0.2751, "depth": 8}
								if obj[6]<=2:
									# {"feature": "Occupation", "instances": 42, "metric_value": 0.3487, "depth": 9}
									if obj[7]>4:
										# {"feature": "Gender", "instances": 26, "metric_value": 0.2168, "depth": 10}
										if obj[3]>0:
											# {"feature": "Passanger", "instances": 22, "metric_value": 0.1515, "depth": 11}
											if obj[0]>1:
												# {"feature": "Direction_same", "instances": 12, "metric_value": 0.1515, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Age", "instances": 11, "metric_value": 0.1558, "depth": 13}
													if obj[4]>0:
														return 'False'
													elif obj[4]<=0:
														return 'False'
													else: return 'False'
												elif obj[11]>0:
													return 'True'
												else: return 'True'
											elif obj[0]<=1:
												return 'False'
											else: return 'False'
										elif obj[3]<=0:
											# {"feature": "Direction_same", "instances": 4, "metric_value": 0.3333, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Passanger", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Age", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[4]<=2:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[11]>0:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[7]<=4:
										# {"feature": "Direction_same", "instances": 16, "metric_value": 0.2812, "depth": 10}
										if obj[11]<=0:
											# {"feature": "Passanger", "instances": 12, "metric_value": 0.3125, "depth": 11}
											if obj[0]<=2:
												# {"feature": "Age", "instances": 8, "metric_value": 0.1667, "depth": 12}
												if obj[4]>0:
													return 'False'
												elif obj[4]<=0:
													# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[3]<=1:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[0]>2:
												# {"feature": "Age", "instances": 4, "metric_value": 0.0, "depth": 12}
												if obj[4]>3:
													return 'False'
												elif obj[4]<=3:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[11]>0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[6]>2:
									# {"feature": "Occupation", "instances": 24, "metric_value": 0.0417, "depth": 9}
									if obj[7]<=7:
										return 'False'
									elif obj[7]>7:
										# {"feature": "Passanger", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[3]<=1:
												# {"feature": "Age", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[4]<=6:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'False'
						elif obj[10]<=0.0:
							# {"feature": "Education", "instances": 67, "metric_value": 0.1598, "depth": 7}
							if obj[6]<=2:
								# {"feature": "Coffeehouse", "instances": 53, "metric_value": 0.0671, "depth": 8}
								if obj[9]>-1.0:
									# {"feature": "Age", "instances": 48, "metric_value": 0.0357, "depth": 9}
									if obj[4]<=6:
										return 'False'
									elif obj[4]>6:
										# {"feature": "Gender", "instances": 7, "metric_value": 0.1429, "depth": 10}
										if obj[3]>0:
											return 'False'
										elif obj[3]<=0:
											# {"feature": "Direction_same", "instances": 2, "metric_value": 0.0, "depth": 11}
											if obj[11]<=0:
												return 'True'
											elif obj[11]>0:
												return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'False'
								elif obj[9]<=-1.0:
									# {"feature": "Passanger", "instances": 5, "metric_value": 0.2667, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Direction_same", "instances": 3, "metric_value": 0.3333, "depth": 10}
										if obj[11]<=0:
											# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Age", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[4]<=6:
													# {"feature": "Occupation", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[7]<=12:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[11]>0:
											return 'False'
										else: return 'False'
									elif obj[0]>1:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[6]>2:
								# {"feature": "Age", "instances": 14, "metric_value": 0.3869, "depth": 8}
								if obj[4]>0:
									# {"feature": "Passanger", "instances": 8, "metric_value": 0.4583, "depth": 9}
									if obj[0]<=2:
										# {"feature": "Occupation", "instances": 6, "metric_value": 0.4167, "depth": 10}
										if obj[7]<=1:
											# {"feature": "Direction_same", "instances": 4, "metric_value": 0.3333, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[3]<=1:
													# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[9]<=0.0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[11]>0:
												return 'False'
											else: return 'False'
										elif obj[7]>1:
											# {"feature": "Direction_same", "instances": 2, "metric_value": 0.0, "depth": 11}
											if obj[11]<=0:
												return 'False'
											elif obj[11]>0:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[0]>2:
										# {"feature": "Occupation", "instances": 2, "metric_value": 0.0, "depth": 10}
										if obj[7]<=1:
											return 'True'
										elif obj[7]>1:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[4]<=0:
									# {"feature": "Passanger", "instances": 6, "metric_value": 0.25, "depth": 9}
									if obj[0]>1:
										# {"feature": "Gender", "instances": 4, "metric_value": 0.375, "depth": 10}
										if obj[3]<=1:
											# {"feature": "Occupation", "instances": 4, "metric_value": 0.375, "depth": 11}
											if obj[7]<=13:
												# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[9]<=0.0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[0]<=1:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[1]>3:
						# {"feature": "Coffeehouse", "instances": 65, "metric_value": 0.1033, "depth": 6}
						if obj[9]>-1.0:
							# {"feature": "Passanger", "instances": 63, "metric_value": 0.0863, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Age", "instances": 32, "metric_value": 0.1597, "depth": 8}
								if obj[4]<=2:
									# {"feature": "Education", "instances": 22, "metric_value": 0.0833, "depth": 9}
									if obj[6]<=1:
										# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.1429, "depth": 10}
										if obj[10]<=1.0:
											# {"feature": "Gender", "instances": 7, "metric_value": 0.2286, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Occupation", "instances": 5, "metric_value": 0.32, "depth": 12}
												if obj[7]<=11:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[3]>0:
												return 'False'
											else: return 'False'
										elif obj[10]>1.0:
											return 'False'
										else: return 'False'
									elif obj[6]>1:
										return 'False'
									else: return 'False'
								elif obj[4]>2:
									# {"feature": "Occupation", "instances": 10, "metric_value": 0.24, "depth": 9}
									if obj[7]<=7:
										return 'False'
									elif obj[7]>7:
										# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.4, "depth": 10}
										if obj[10]>-1.0:
											# {"feature": "Gender", "instances": 4, "metric_value": 0.5, "depth": 11}
											if obj[3]>0:
												# {"feature": "Education", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[6]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Education", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[6]<=3:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[10]<=-1.0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[0]>1:
								return 'False'
							else: return 'False'
						elif obj[9]<=-1.0:
							# {"feature": "Passanger", "instances": 2, "metric_value": 0.0, "depth": 7}
							if obj[0]<=2:
								return 'False'
							elif obj[0]>2:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'False'
				elif obj[12]>2:
					# {"feature": "Passanger", "instances": 96, "metric_value": 0.1141, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Education", "instances": 92, "metric_value": 0.0831, "depth": 6}
						if obj[6]<=4:
							# {"feature": "Occupation", "instances": 91, "metric_value": 0.0637, "depth": 7}
							if obj[7]<=22:
								# {"feature": "Gender", "instances": 90, "metric_value": 0.0635, "depth": 8}
								if obj[3]>0:
									# {"feature": "Time", "instances": 64, "metric_value": 0.0882, "depth": 9}
									if obj[1]>0:
										# {"feature": "Age", "instances": 51, "metric_value": 0.1091, "depth": 10}
										if obj[4]<=4:
											# {"feature": "Restaurant20to50", "instances": 43, "metric_value": 0.084, "depth": 11}
											if obj[10]>0.0:
												# {"feature": "Coffeehouse", "instances": 37, "metric_value": 0.0491, "depth": 12}
												if obj[9]<=2.0:
													return 'False'
												elif obj[9]>2.0:
													# {"feature": "Direction_same", "instances": 11, "metric_value": 0.1653, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[10]<=0.0:
												# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.25, "depth": 12}
												if obj[9]<=0.0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[9]>0.0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[4]>4:
											# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.1667, "depth": 11}
											if obj[10]<=1.0:
												return 'False'
											elif obj[10]>1.0:
												# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.3333, "depth": 12}
												if obj[9]<=2.0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[9]>2.0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[1]<=0:
										return 'False'
									else: return 'False'
								elif obj[3]<=0:
									return 'False'
								else: return 'False'
							elif obj[7]>22:
								return 'True'
							else: return 'True'
						elif obj[6]>4:
							return 'True'
						else: return 'True'
					elif obj[0]>1:
						# {"feature": "Education", "instances": 4, "metric_value": 0.0, "depth": 6}
						if obj[6]>1:
							return 'True'
						elif obj[6]<=1:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			elif obj[5]<=0:
				# {"feature": "Occupation", "instances": 446, "metric_value": 0.4309, "depth": 4}
				if obj[7]>2:
					# {"feature": "Restaurant20to50", "instances": 345, "metric_value": 0.4641, "depth": 5}
					if obj[10]<=3.0:
						# {"feature": "Education", "instances": 340, "metric_value": 0.4643, "depth": 6}
						if obj[6]>1:
							# {"feature": "Age", "instances": 189, "metric_value": 0.4245, "depth": 7}
							if obj[4]>0:
								# {"feature": "Coffeehouse", "instances": 164, "metric_value": 0.4048, "depth": 8}
								if obj[9]<=2.0:
									# {"feature": "Passanger", "instances": 145, "metric_value": 0.4258, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Distance", "instances": 126, "metric_value": 0.4103, "depth": 10}
										if obj[12]>1:
											# {"feature": "Direction_same", "instances": 78, "metric_value": 0.3684, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Time", "instances": 71, "metric_value": 0.3927, "depth": 12}
												if obj[1]<=3:
													# {"feature": "Gender", "instances": 66, "metric_value": 0.4209, "depth": 13}
													if obj[3]<=0:
														return 'False'
													elif obj[3]>0:
														return 'False'
													else: return 'False'
												elif obj[1]>3:
													return 'False'
												else: return 'False'
											elif obj[11]>0:
												return 'False'
											else: return 'False'
										elif obj[12]<=1:
											# {"feature": "Time", "instances": 48, "metric_value": 0.4549, "depth": 11}
											if obj[1]>0:
												# {"feature": "Direction_same", "instances": 25, "metric_value": 0.4174, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Gender", "instances": 23, "metric_value": 0.4328, "depth": 13}
													if obj[3]>0:
														return 'False'
													elif obj[3]<=0:
														return 'False'
													else: return 'False'
												elif obj[11]>0:
													return 'False'
												else: return 'False'
											elif obj[1]<=0:
												# {"feature": "Gender", "instances": 23, "metric_value": 0.4228, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 17, "metric_value": 0.4152, "depth": 13}
													if obj[11]<=1:
														return 'False'
													else: return 'False'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=1:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'False'
										else: return 'False'
									elif obj[0]>1:
										# {"feature": "Time", "instances": 19, "metric_value": 0.498, "depth": 10}
										if obj[1]<=3:
											# {"feature": "Gender", "instances": 13, "metric_value": 0.4718, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 10, "metric_value": 0.48, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 10, "metric_value": 0.48, "depth": 13}
													if obj[12]<=2:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[12]<=2:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[1]>3:
											# {"feature": "Gender", "instances": 6, "metric_value": 0.4444, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[12]<=1:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[12]<=1:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'False'
									else: return 'False'
								elif obj[9]>2.0:
									# {"feature": "Time", "instances": 19, "metric_value": 0.1517, "depth": 9}
									if obj[1]<=3:
										# {"feature": "Direction_same", "instances": 17, "metric_value": 0.0588, "depth": 10}
										if obj[11]<=0:
											return 'False'
										elif obj[11]>0:
											# {"feature": "Gender", "instances": 2, "metric_value": 0.0, "depth": 11}
											if obj[3]>0:
												return 'True'
											elif obj[3]<=0:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[1]>3:
										# {"feature": "Passanger", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[0]<=0:
											# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[3]<=1:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[12]<=1:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[4]<=0:
								# {"feature": "Coffeehouse", "instances": 25, "metric_value": 0.4241, "depth": 8}
								if obj[9]<=1.0:
									# {"feature": "Direction_same", "instances": 18, "metric_value": 0.4479, "depth": 9}
									if obj[11]<=0:
										# {"feature": "Time", "instances": 13, "metric_value": 0.4196, "depth": 10}
										if obj[1]>0:
											# {"feature": "Distance", "instances": 11, "metric_value": 0.4545, "depth": 11}
											if obj[12]<=2:
												# {"feature": "Gender", "instances": 10, "metric_value": 0.4444, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Passanger", "instances": 9, "metric_value": 0.4444, "depth": 13}
													if obj[0]>0:
														return 'False'
													elif obj[0]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											elif obj[12]>2:
												return 'False'
											else: return 'False'
										elif obj[1]<=0:
											return 'True'
										else: return 'True'
									elif obj[11]>0:
										# {"feature": "Time", "instances": 5, "metric_value": 0.2667, "depth": 10}
										if obj[1]>0:
											# {"feature": "Passanger", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Distance", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[12]<=2:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[1]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[9]>1.0:
									# {"feature": "Distance", "instances": 7, "metric_value": 0.1429, "depth": 9}
									if obj[12]<=2:
										return 'True'
									elif obj[12]>2:
										# {"feature": "Passanger", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Time", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[1]<=1:
												# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[3]<=1:
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
						elif obj[6]<=1:
							# {"feature": "Coffeehouse", "instances": 151, "metric_value": 0.4768, "depth": 7}
							if obj[9]>-1.0:
								# {"feature": "Gender", "instances": 147, "metric_value": 0.4835, "depth": 8}
								if obj[3]<=0:
									# {"feature": "Age", "instances": 91, "metric_value": 0.4598, "depth": 9}
									if obj[4]<=6:
										# {"feature": "Time", "instances": 87, "metric_value": 0.4749, "depth": 10}
										if obj[1]<=2:
											# {"feature": "Passanger", "instances": 53, "metric_value": 0.4547, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Distance", "instances": 48, "metric_value": 0.4616, "depth": 12}
												if obj[12]<=2:
													# {"feature": "Direction_same", "instances": 31, "metric_value": 0.4776, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												elif obj[12]>2:
													# {"feature": "Direction_same", "instances": 17, "metric_value": 0.4152, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[0]>1:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[12]<=2:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[1]>2:
											# {"feature": "Direction_same", "instances": 34, "metric_value": 0.444, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Passanger", "instances": 31, "metric_value": 0.4766, "depth": 12}
												if obj[0]>0:
													# {"feature": "Distance", "instances": 24, "metric_value": 0.4852, "depth": 13}
													if obj[12]>1:
														return 'False'
													elif obj[12]<=1:
														return 'True'
													else: return 'True'
												elif obj[0]<=0:
													# {"feature": "Distance", "instances": 7, "metric_value": 0.381, "depth": 13}
													if obj[12]<=1:
														return 'False'
													elif obj[12]>1:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[11]>0:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[4]>6:
										return 'False'
									else: return 'False'
								elif obj[3]>0:
									# {"feature": "Time", "instances": 56, "metric_value": 0.4797, "depth": 9}
									if obj[1]>0:
										# {"feature": "Direction_same", "instances": 41, "metric_value": 0.4767, "depth": 10}
										if obj[11]<=0:
											# {"feature": "Age", "instances": 36, "metric_value": 0.4833, "depth": 11}
											if obj[4]<=5:
												# {"feature": "Passanger", "instances": 30, "metric_value": 0.4795, "depth": 12}
												if obj[0]>0:
													# {"feature": "Distance", "instances": 23, "metric_value": 0.4666, "depth": 13}
													if obj[12]>1:
														return 'False'
													elif obj[12]<=1:
														return 'False'
													else: return 'False'
												elif obj[0]<=0:
													# {"feature": "Distance", "instances": 7, "metric_value": 0.381, "depth": 13}
													if obj[12]<=1:
														return 'True'
													elif obj[12]>1:
														return 'False'
													else: return 'False'
												else: return 'True'
											elif obj[4]>5:
												# {"feature": "Distance", "instances": 6, "metric_value": 0.2667, "depth": 12}
												if obj[12]>1:
													# {"feature": "Passanger", "instances": 5, "metric_value": 0.2667, "depth": 13}
													if obj[0]<=1:
														return 'True'
													elif obj[0]>1:
														return 'True'
													else: return 'True'
												elif obj[12]<=1:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[11]>0:
											# {"feature": "Age", "instances": 5, "metric_value": 0.2667, "depth": 11}
											if obj[4]<=4:
												# {"feature": "Passanger", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Distance", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[12]<=2:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[4]>4:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[1]<=0:
										# {"feature": "Distance", "instances": 15, "metric_value": 0.3077, "depth": 10}
										if obj[12]<=2:
											# {"feature": "Age", "instances": 13, "metric_value": 0.2906, "depth": 11}
											if obj[4]>1:
												# {"feature": "Direction_same", "instances": 9, "metric_value": 0.1852, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Passanger", "instances": 6, "metric_value": 0.2667, "depth": 13}
													if obj[0]>0:
														return 'True'
													elif obj[0]<=0:
														return 'True'
													else: return 'True'
												elif obj[11]>0:
													return 'True'
												else: return 'True'
											elif obj[4]<=1:
												# {"feature": "Passanger", "instances": 4, "metric_value": 0.3333, "depth": 12}
												if obj[0]>0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.3333, "depth": 13}
													if obj[11]>0:
														return 'False'
													elif obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[0]<=0:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[12]>2:
											return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'False'
							elif obj[9]<=-1.0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[10]>3.0:
						return 'True'
					else: return 'True'
				elif obj[7]<=2:
					# {"feature": "Age", "instances": 101, "metric_value": 0.2574, "depth": 5}
					if obj[4]<=4:
						# {"feature": "Coffeehouse", "instances": 66, "metric_value": 0.153, "depth": 6}
						if obj[9]>0.0:
							# {"feature": "Passanger", "instances": 39, "metric_value": 0.041, "depth": 7}
							if obj[0]<=1:
								return 'False'
							elif obj[0]>1:
								# {"feature": "Time", "instances": 5, "metric_value": 0.2, "depth": 8}
								if obj[1]>2:
									return 'False'
								elif obj[1]<=2:
									# {"feature": "Gender", "instances": 2, "metric_value": 0.0, "depth": 9}
									if obj[3]>0:
										return 'False'
									elif obj[3]<=0:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'False'
						elif obj[9]<=0.0:
							# {"feature": "Direction_same", "instances": 27, "metric_value": 0.2778, "depth": 7}
							if obj[11]<=0:
								# {"feature": "Passanger", "instances": 20, "metric_value": 0.3438, "depth": 8}
								if obj[0]<=1:
									# {"feature": "Education", "instances": 16, "metric_value": 0.3846, "depth": 9}
									if obj[6]<=2:
										# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.3547, "depth": 10}
										if obj[10]<=0.0:
											# {"feature": "Gender", "instances": 9, "metric_value": 0.2667, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Time", "instances": 5, "metric_value": 0.4667, "depth": 12}
												if obj[1]>1:
													# {"feature": "Distance", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[12]<=1:
														return 'False'
													else: return 'False'
												elif obj[1]<=1:
													# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[12]<=3:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]>0:
												return 'False'
											else: return 'False'
										elif obj[10]>0.0:
											# {"feature": "Gender", "instances": 4, "metric_value": 0.0, "depth": 11}
											if obj[3]>0:
												return 'True'
											elif obj[3]<=0:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[6]>2:
										return 'False'
									else: return 'False'
								elif obj[0]>1:
									return 'False'
								else: return 'False'
							elif obj[11]>0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[4]>4:
						# {"feature": "Coffeehouse", "instances": 35, "metric_value": 0.2743, "depth": 6}
						if obj[9]<=1.0:
							# {"feature": "Passanger", "instances": 30, "metric_value": 0.275, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Education", "instances": 24, "metric_value": 0.1932, "depth": 8}
								if obj[6]<=3:
									# {"feature": "Gender", "instances": 22, "metric_value": 0.1558, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Direction_same", "instances": 14, "metric_value": 0.2286, "depth": 10}
										if obj[11]<=0:
											# {"feature": "Time", "instances": 10, "metric_value": 0.3, "depth": 11}
											if obj[1]<=2:
												# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.375, "depth": 12}
												if obj[10]<=1.0:
													# {"feature": "Distance", "instances": 8, "metric_value": 0.375, "depth": 13}
													if obj[12]>1:
														return 'False'
													elif obj[12]<=1:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[1]>2:
												return 'False'
											else: return 'False'
										elif obj[11]>0:
											return 'False'
										else: return 'False'
									elif obj[3]>0:
										return 'False'
									else: return 'False'
								elif obj[6]>3:
									# {"feature": "Time", "instances": 2, "metric_value": 0.0, "depth": 9}
									if obj[1]<=0:
										return 'False'
									elif obj[1]>0:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[0]>1:
								# {"feature": "Time", "instances": 6, "metric_value": 0.4, "depth": 8}
								if obj[1]<=3:
									# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.3, "depth": 9}
									if obj[10]<=1.0:
										# {"feature": "Gender", "instances": 4, "metric_value": 0.25, "depth": 10}
										if obj[3]>0:
											return 'True'
										elif obj[3]<=0:
											# {"feature": "Education", "instances": 2, "metric_value": 0.0, "depth": 11}
											if obj[6]>0:
												return 'False'
											elif obj[6]<=0:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[10]>1.0:
										return 'False'
									else: return 'False'
								elif obj[1]>3:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[9]>1.0:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'False'
