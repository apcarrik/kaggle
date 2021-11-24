def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Education", "instances": 127, "metric_value": 1.0, "depth": 1}
	if obj[8]<=3:
		# {"feature": "Income", "instances": 121, "metric_value": 0.9988, "depth": 2}
		if obj[10]<=7:
			# {"feature": "Coupon_validity", "instances": 108, "metric_value": 0.9878, "depth": 3}
			if obj[4]<=0:
				# {"feature": "Coupon", "instances": 57, "metric_value": 0.9944, "depth": 4}
				if obj[3]<=2:
					# {"feature": "Time", "instances": 31, "metric_value": 0.9383, "depth": 5}
					if obj[2]<=3:
						# {"feature": "Occupation", "instances": 27, "metric_value": 0.9751, "depth": 6}
						if obj[9]<=11:
							# {"feature": "Direction_same", "instances": 23, "metric_value": 0.8865, "depth": 7}
							if obj[14]<=0:
								# {"feature": "Bar", "instances": 17, "metric_value": 0.9774, "depth": 8}
								if obj[11]>0.0:
									# {"feature": "Coffeehouse", "instances": 12, "metric_value": 0.8113, "depth": 9}
									if obj[12]>0.0:
										# {"feature": "Gender", "instances": 9, "metric_value": 0.5033, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 11}
											if obj[6]>1:
												return 'False'
											elif obj[6]<=1:
												return 'True'
											else: return 'True'
										elif obj[5]>0:
											return 'False'
										else: return 'False'
									elif obj[12]<=0.0:
										# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[1]<=1:
											return 'True'
										elif obj[1]>1:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[11]<=0.0:
									# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[6]>0:
										return 'True'
									elif obj[6]<=0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[14]>0:
								return 'False'
							else: return 'False'
						elif obj[9]>11:
							return 'True'
						else: return 'True'
					elif obj[2]>3:
						return 'False'
					else: return 'False'
				elif obj[3]>2:
					# {"feature": "Coffeehouse", "instances": 26, "metric_value": 0.7793, "depth": 5}
					if obj[12]>1.0:
						# {"feature": "Age", "instances": 15, "metric_value": 0.3534, "depth": 6}
						if obj[6]>0:
							return 'True'
						elif obj[6]<=0:
							# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[11]>1.0:
								return 'True'
							elif obj[11]<=1.0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[12]<=1.0:
						# {"feature": "Passanger", "instances": 11, "metric_value": 0.994, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Occupation", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[9]>2:
								return 'False'
							elif obj[9]<=2:
								return 'True'
							else: return 'True'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[4]>0:
				# {"feature": "Coffeehouse", "instances": 51, "metric_value": 0.8974, "depth": 4}
				if obj[12]<=3.0:
					# {"feature": "Occupation", "instances": 44, "metric_value": 0.9457, "depth": 5}
					if obj[9]<=12:
						# {"feature": "Passanger", "instances": 39, "metric_value": 0.9766, "depth": 6}
						if obj[0]>0:
							# {"feature": "Bar", "instances": 35, "metric_value": 0.9518, "depth": 7}
							if obj[11]<=2.0:
								# {"feature": "Restaurant20to50", "instances": 34, "metric_value": 0.9367, "depth": 8}
								if obj[13]<=2.0:
									# {"feature": "Coupon", "instances": 31, "metric_value": 0.9629, "depth": 9}
									if obj[3]>0:
										# {"feature": "Gender", "instances": 29, "metric_value": 0.9784, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Distance", "instances": 16, "metric_value": 0.896, "depth": 11}
											if obj[15]<=2:
												# {"feature": "Age", "instances": 11, "metric_value": 0.994, "depth": 12}
												if obj[6]>2:
													# {"feature": "Weather", "instances": 7, "metric_value": 0.9852, "depth": 13}
													if obj[1]<=0:
														# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 14}
														if obj[2]>0:
															# {"feature": "Children", "instances": 5, "metric_value": 0.971, "depth": 15}
															if obj[7]>0:
																# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[14]<=0:
																	return 'True'
																else: return 'True'
															elif obj[7]<=0:
																# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[14]<=0:
																	return 'False'
																else: return 'False'
															else: return 'False'
														elif obj[2]<=0:
															return 'True'
														else: return 'True'
													elif obj[1]>0:
														return 'False'
													else: return 'False'
												elif obj[6]<=2:
													# {"feature": "Weather", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[1]<=0:
														return 'False'
													elif obj[1]>0:
														return 'True'
													else: return 'True'
												else: return 'False'
											elif obj[15]>2:
												return 'False'
											else: return 'False'
										elif obj[5]>0:
											# {"feature": "Age", "instances": 13, "metric_value": 0.9957, "depth": 11}
											if obj[6]<=6:
												# {"feature": "Distance", "instances": 11, "metric_value": 0.9457, "depth": 12}
												if obj[15]>1:
													# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 13}
													if obj[2]<=3:
														return 'True'
													elif obj[2]>3:
														# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[1]<=0:
															# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[7]<=1:
																# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[14]<=0:
																	return 'False'
																else: return 'False'
															else: return 'False'
														else: return 'False'
													else: return 'False'
												elif obj[15]<=1:
													# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 13}
													if obj[2]<=2:
														# {"feature": "Weather", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[1]<=0:
															# {"feature": "Children", "instances": 4, "metric_value": 0.8113, "depth": 15}
															if obj[7]<=1:
																# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 16}
																if obj[14]<=0:
																	return 'False'
																else: return 'False'
															else: return 'False'
														else: return 'False'
													elif obj[2]>2:
														return 'True'
													else: return 'True'
												else: return 'False'
											elif obj[6]>6:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[3]<=0:
										return 'False'
									else: return 'False'
								elif obj[13]>2.0:
									return 'False'
								else: return 'False'
							elif obj[11]>2.0:
								return 'True'
							else: return 'True'
						elif obj[0]<=0:
							# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[2]>0:
								return 'True'
							elif obj[2]<=0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[9]>12:
						return 'False'
					else: return 'False'
				elif obj[12]>3.0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[10]>7:
			# {"feature": "Occupation", "instances": 13, "metric_value": 0.6194, "depth": 3}
			if obj[9]>3:
				return 'True'
			elif obj[9]<=3:
				# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[14]>0:
					return 'True'
				elif obj[14]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[8]>3:
		return 'True'
	else: return 'True'
