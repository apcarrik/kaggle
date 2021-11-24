def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Age", "instances": 51, "metric_value": 0.9931, "depth": 1}
	if obj[6]<=6:
		# {"feature": "Occupation", "instances": 47, "metric_value": 0.9997, "depth": 2}
		if obj[9]<=14:
			# {"feature": "Restaurant20to50", "instances": 44, "metric_value": 0.994, "depth": 3}
			if obj[13]<=2.0:
				# {"feature": "Distance", "instances": 41, "metric_value": 0.9789, "depth": 4}
				if obj[15]<=2:
					# {"feature": "Income", "instances": 38, "metric_value": 0.9495, "depth": 5}
					if obj[10]>0:
						# {"feature": "Weather", "instances": 35, "metric_value": 0.971, "depth": 6}
						if obj[1]<=0:
							# {"feature": "Coffeehouse", "instances": 30, "metric_value": 0.9183, "depth": 7}
							if obj[12]<=3.0:
								# {"feature": "Coupon", "instances": 28, "metric_value": 0.8631, "depth": 8}
								if obj[3]>1:
									# {"feature": "Education", "instances": 16, "metric_value": 0.6962, "depth": 9}
									if obj[8]<=2:
										return 'True'
									elif obj[8]>2:
										# {"feature": "Gender", "instances": 7, "metric_value": 0.9852, "depth": 10}
										if obj[5]>0:
											# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 11}
											if obj[0]>1:
												return 'True'
											elif obj[0]<=1:
												# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[11]<=1.0:
													return 'True'
												elif obj[11]>1.0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[5]<=0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[3]<=1:
									# {"feature": "Time", "instances": 12, "metric_value": 0.9799, "depth": 9}
									if obj[2]<=3:
										# {"feature": "Passanger", "instances": 10, "metric_value": 0.8813, "depth": 10}
										if obj[0]>0:
											# {"feature": "Bar", "instances": 9, "metric_value": 0.9183, "depth": 11}
											if obj[11]<=1.0:
												# {"feature": "Gender", "instances": 8, "metric_value": 0.8113, "depth": 12}
												if obj[5]<=0:
													return 'True'
												elif obj[5]>0:
													# {"feature": "Coupon_validity", "instances": 4, "metric_value": 1.0, "depth": 13}
													if obj[4]<=0:
														# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[14]<=0:
															return 'True'
														elif obj[14]>0:
															return 'False'
														else: return 'False'
													elif obj[4]>0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[11]>1.0:
												return 'False'
											else: return 'False'
										elif obj[0]<=0:
											return 'True'
										else: return 'True'
									elif obj[2]>3:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[12]>3.0:
								return 'False'
							else: return 'False'
						elif obj[1]>0:
							# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[8]<=3:
								return 'False'
							elif obj[8]>3:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[10]<=0:
						return 'True'
					else: return 'True'
				elif obj[15]>2:
					return 'False'
				else: return 'False'
			elif obj[13]>2.0:
				return 'False'
			else: return 'False'
		elif obj[9]>14:
			return 'False'
		else: return 'False'
	elif obj[6]>6:
		return 'True'
	else: return 'True'
