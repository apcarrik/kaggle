def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Distance", "instances": 51, "metric_value": 0.9774, "depth": 1}
	if obj[17]<=2:
		# {"feature": "Occupation", "instances": 45, "metric_value": 0.9183, "depth": 2}
		if obj[10]<=17:
			# {"feature": "Coupon", "instances": 42, "metric_value": 0.8631, "depth": 3}
			if obj[3]<=3:
				# {"feature": "Age", "instances": 26, "metric_value": 0.6194, "depth": 4}
				if obj[6]<=3:
					# {"feature": "Bar", "instances": 17, "metric_value": 0.7871, "depth": 5}
					if obj[12]>0.0:
						# {"feature": "Coffeehouse", "instances": 12, "metric_value": 0.9183, "depth": 6}
						if obj[13]<=2.0:
							# {"feature": "Education", "instances": 8, "metric_value": 1.0, "depth": 7}
							if obj[9]<=2:
								# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[2]>1:
									# {"feature": "Weather", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[1]<=0:
										# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[0]>1:
											# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[4]<=1:
												# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[5]<=1:
													# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7]<=0:
														# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[8]<=0:
															# {"feature": "Income", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[11]<=0:
																# {"feature": "Restaurantlessthan20", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[14]<=3.0:
																	# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[15]<=1.0:
																		# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[16]<=0:
																			return 'True'
																		else: return 'True'
																	else: return 'True'
																else: return 'True'
															else: return 'True'
														else: return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[0]<=1:
											return 'False'
										else: return 'False'
									elif obj[1]>0:
										return 'True'
									else: return 'True'
								elif obj[2]<=1:
									return 'True'
								else: return 'True'
							elif obj[9]>2:
								return 'False'
							else: return 'False'
						elif obj[13]>2.0:
							return 'True'
						else: return 'True'
					elif obj[12]<=0.0:
						return 'True'
					else: return 'True'
				elif obj[6]>3:
					return 'True'
				else: return 'True'
			elif obj[3]>3:
				# {"feature": "Bar", "instances": 16, "metric_value": 1.0, "depth": 4}
				if obj[12]<=1.0:
					# {"feature": "Coffeehouse", "instances": 14, "metric_value": 0.9852, "depth": 5}
					if obj[13]<=2.0:
						# {"feature": "Income", "instances": 10, "metric_value": 0.971, "depth": 6}
						if obj[11]>1:
							# {"feature": "Passanger", "instances": 8, "metric_value": 0.8113, "depth": 7}
							if obj[0]<=1:
								return 'False'
							elif obj[0]>1:
								# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[2]<=0:
									# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[6]>1:
										return 'True'
									elif obj[6]<=1:
										return 'False'
									else: return 'False'
								elif obj[2]>0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[11]<=1:
							return 'True'
						else: return 'True'
					elif obj[13]>2.0:
						return 'True'
					else: return 'True'
				elif obj[12]>1.0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[10]>17:
			return 'False'
		else: return 'False'
	elif obj[17]>2:
		return 'False'
	else: return 'False'
