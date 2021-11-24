def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Time", "instances": 34, "metric_value": 0.874, "depth": 1}
	if obj[2]<=3:
		# {"feature": "Weather", "instances": 26, "metric_value": 0.9612, "depth": 2}
		if obj[1]<=0:
			# {"feature": "Income", "instances": 23, "metric_value": 0.8865, "depth": 3}
			if obj[10]<=3:
				# {"feature": "Occupation", "instances": 13, "metric_value": 0.9957, "depth": 4}
				if obj[9]<=11:
					# {"feature": "Coupon", "instances": 11, "metric_value": 0.9457, "depth": 5}
					if obj[3]>0:
						# {"feature": "Coupon_validity", "instances": 10, "metric_value": 0.8813, "depth": 6}
						if obj[4]>0:
							# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[0]>1:
								# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[12]<=1.0:
									# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[6]>1:
										# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[5]<=1:
											# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[7]<=0:
												# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[8]<=2:
													# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[11]<=0.0:
														# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[13]<=0.0:
															# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[14]<=0:
																# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[15]<=2:
																	return 'True'
																else: return 'True'
															else: return 'True'
														else: return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[6]<=1:
										return 'False'
									else: return 'False'
								elif obj[12]>1.0:
									return 'True'
								else: return 'True'
							elif obj[0]<=1:
								return 'False'
							else: return 'False'
						elif obj[4]<=0:
							return 'True'
						else: return 'True'
					elif obj[3]<=0:
						return 'False'
					else: return 'False'
				elif obj[9]>11:
					return 'False'
				else: return 'False'
			elif obj[10]>3:
				# {"feature": "Coupon", "instances": 10, "metric_value": 0.469, "depth": 4}
				if obj[3]<=3:
					return 'True'
				elif obj[3]>3:
					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]<=1:
						return 'False'
					elif obj[0]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		elif obj[1]>0:
			return 'False'
		else: return 'False'
	elif obj[2]>3:
		return 'True'
	else: return 'True'
