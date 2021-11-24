def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Passanger", "instances": 51, "metric_value": 0.9975, "depth": 1}
	if obj[1]<=2:
		# {"feature": "Income", "instances": 40, "metric_value": 0.9928, "depth": 2}
		if obj[13]>1:
			# {"feature": "Restaurantlessthan20", "instances": 37, "metric_value": 0.974, "depth": 3}
			if obj[16]<=3.0:
				# {"feature": "Weather", "instances": 35, "metric_value": 0.9518, "depth": 4}
				if obj[2]<=0:
					# {"feature": "Occupation", "instances": 27, "metric_value": 0.9911, "depth": 5}
					if obj[12]<=18:
						# {"feature": "Coupon", "instances": 25, "metric_value": 0.9988, "depth": 6}
						if obj[5]>1:
							# {"feature": "Maritalstatus", "instances": 17, "metric_value": 0.9774, "depth": 7}
							if obj[9]<=1:
								# {"feature": "Time", "instances": 13, "metric_value": 0.8905, "depth": 8}
								if obj[4]<=1:
									# {"feature": "Age", "instances": 9, "metric_value": 0.9911, "depth": 9}
									if obj[8]>0:
										# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.9544, "depth": 10}
										if obj[15]>1.0:
											# {"feature": "Driving_to", "instances": 6, "metric_value": 1.0, "depth": 11}
											if obj[0]>0:
												# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 12}
												if obj[7]<=0:
													# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[3]<=55:
														# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[6]<=0:
															# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[10]<=1:
																# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[11]<=0:
																	# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[14]<=0.0:
																		# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[17]<=1.0:
																			# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[18]<=0:
																				# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[19]<=1:
																					return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	else: return 'False'
																else: return 'False'
															else: return 'False'
														else: return 'False'
													elif obj[3]>55:
														return 'True'
													else: return 'True'
												elif obj[7]>0:
													return 'False'
												else: return 'False'
											elif obj[0]<=0:
												return 'True'
											else: return 'True'
										elif obj[15]<=1.0:
											return 'True'
										else: return 'True'
									elif obj[8]<=0:
										return 'False'
									else: return 'False'
								elif obj[4]>1:
									return 'True'
								else: return 'True'
							elif obj[9]>1:
								# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[8]<=1:
									return 'False'
								elif obj[8]>1:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[5]<=1:
							# {"feature": "Education", "instances": 8, "metric_value": 0.8113, "depth": 7}
							if obj[11]>2:
								# {"feature": "Driving_to", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[0]<=1:
									# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[8]<=5:
										return 'False'
									elif obj[8]>5:
										return 'True'
									else: return 'True'
								elif obj[0]>1:
									return 'True'
								else: return 'True'
							elif obj[11]<=2:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[12]>18:
						return 'False'
					else: return 'False'
				elif obj[2]>0:
					# {"feature": "Occupation", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[12]<=14:
						return 'False'
					elif obj[12]>14:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[16]>3.0:
				return 'True'
			else: return 'True'
		elif obj[13]<=1:
			return 'True'
		else: return 'True'
	elif obj[1]>2:
		# {"feature": "Occupation", "instances": 11, "metric_value": 0.684, "depth": 2}
		if obj[12]<=9:
			return 'True'
		elif obj[12]>9:
			return 'False'
		else: return 'False'
	else: return 'True'
