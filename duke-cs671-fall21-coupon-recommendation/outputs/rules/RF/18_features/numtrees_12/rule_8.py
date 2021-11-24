def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Distance", "instances": 85, "metric_value": 0.9999, "depth": 1}
	if obj[17]<=2:
		# {"feature": "Maritalstatus", "instances": 74, "metric_value": 0.9868, "depth": 2}
		if obj[7]<=2:
			# {"feature": "Age", "instances": 70, "metric_value": 0.971, "depth": 3}
			if obj[6]<=6:
				# {"feature": "Education", "instances": 63, "metric_value": 0.9334, "depth": 4}
				if obj[9]<=3:
					# {"feature": "Passanger", "instances": 59, "metric_value": 0.9529, "depth": 5}
					if obj[0]>0:
						# {"feature": "Occupation", "instances": 54, "metric_value": 0.9183, "depth": 6}
						if obj[10]<=19:
							# {"feature": "Direction_same", "instances": 53, "metric_value": 0.9052, "depth": 7}
							if obj[16]<=0:
								# {"feature": "Coupon_validity", "instances": 42, "metric_value": 0.9587, "depth": 8}
								if obj[4]<=0:
									# {"feature": "Income", "instances": 23, "metric_value": 0.7554, "depth": 9}
									if obj[11]<=7:
										# {"feature": "Restaurant20to50", "instances": 22, "metric_value": 0.684, "depth": 10}
										if obj[15]<=1.0:
											# {"feature": "Coupon", "instances": 17, "metric_value": 0.7871, "depth": 11}
											if obj[3]>1:
												# {"feature": "Gender", "instances": 14, "metric_value": 0.5917, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Bar", "instances": 8, "metric_value": 0.8113, "depth": 13}
													if obj[12]<=0.0:
														# {"feature": "Weather", "instances": 4, "metric_value": 1.0, "depth": 14}
														if obj[1]<=0:
															# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[2]>1:
																return 'False'
															elif obj[2]<=1:
																return 'True'
															else: return 'True'
														elif obj[1]>0:
															return 'True'
														else: return 'True'
													elif obj[12]>0.0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													return 'True'
												else: return 'True'
											elif obj[3]<=1:
												# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[13]>1.0:
													return 'False'
												elif obj[13]<=1.0:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[15]>1.0:
											return 'True'
										else: return 'True'
									elif obj[11]>7:
										return 'False'
									else: return 'False'
								elif obj[4]>0:
									# {"feature": "Coffeehouse", "instances": 19, "metric_value": 0.9819, "depth": 9}
									if obj[13]<=3.0:
										# {"feature": "Bar", "instances": 17, "metric_value": 0.9975, "depth": 10}
										if obj[12]<=2.0:
											# {"feature": "Coupon", "instances": 15, "metric_value": 0.971, "depth": 11}
											if obj[3]<=3:
												# {"feature": "Time", "instances": 9, "metric_value": 0.9183, "depth": 12}
												if obj[2]>2:
													# {"feature": "Weather", "instances": 6, "metric_value": 1.0, "depth": 13}
													if obj[1]<=0:
														# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[5]>0:
															return 'True'
														elif obj[5]<=0:
															return 'False'
														else: return 'False'
													elif obj[1]>0:
														return 'False'
													else: return 'False'
												elif obj[2]<=2:
													return 'True'
												else: return 'True'
											elif obj[3]>3:
												return 'False'
											else: return 'False'
										elif obj[12]>2.0:
											return 'True'
										else: return 'True'
									elif obj[13]>3.0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[16]>0:
								# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.4395, "depth": 8}
								if obj[13]<=2.0:
									return 'True'
								elif obj[13]>2.0:
									# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[3]<=1:
										return 'False'
									elif obj[3]>1:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'True'
						elif obj[10]>19:
							return 'False'
						else: return 'False'
					elif obj[0]<=0:
						# {"feature": "Income", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[11]>0:
							return 'False'
						elif obj[11]<=0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[9]>3:
					return 'True'
				else: return 'True'
			elif obj[6]>6:
				# {"feature": "Occupation", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[10]<=22:
					return 'False'
				elif obj[10]>22:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[7]>2:
			return 'False'
		else: return 'False'
	elif obj[17]>2:
		# {"feature": "Income", "instances": 11, "metric_value": 0.4395, "depth": 2}
		if obj[11]<=4:
			return 'False'
		elif obj[11]>4:
			# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[1]<=0:
				return 'True'
			elif obj[1]>0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
