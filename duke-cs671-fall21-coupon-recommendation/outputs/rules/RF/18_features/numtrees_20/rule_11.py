def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9367, "depth": 1}
	if obj[3]>1:
		# {"feature": "Age", "instances": 39, "metric_value": 0.9881, "depth": 2}
		if obj[6]<=5:
			# {"feature": "Income", "instances": 34, "metric_value": 1.0, "depth": 3}
			if obj[11]<=5:
				# {"feature": "Bar", "instances": 27, "metric_value": 0.9751, "depth": 4}
				if obj[12]<=3.0:
					# {"feature": "Restaurantlessthan20", "instances": 25, "metric_value": 0.9427, "depth": 5}
					if obj[14]>0.0:
						# {"feature": "Direction_same", "instances": 23, "metric_value": 0.8865, "depth": 6}
						if obj[16]<=0:
							# {"feature": "Occupation", "instances": 18, "metric_value": 0.9641, "depth": 7}
							if obj[10]<=18:
								# {"feature": "Coffeehouse", "instances": 16, "metric_value": 0.896, "depth": 8}
								if obj[13]>0.0:
									# {"feature": "Coupon_validity", "instances": 12, "metric_value": 0.9799, "depth": 9}
									if obj[4]>0:
										# {"feature": "Time", "instances": 8, "metric_value": 0.8113, "depth": 10}
										if obj[2]>0:
											# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 11}
											if obj[9]>0:
												# {"feature": "Weather", "instances": 4, "metric_value": 0.8113, "depth": 12}
												if obj[1]<=0:
													return 'False'
												elif obj[1]>0:
													# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[0]>0:
														return 'True'
													elif obj[0]<=0:
														return 'False'
													else: return 'False'
												else: return 'True'
											elif obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[2]<=0:
											return 'False'
										else: return 'False'
									elif obj[4]<=0:
										# {"feature": "Maritalstatus", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[7]>0:
											return 'True'
										elif obj[7]<=0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[13]<=0.0:
									return 'False'
								else: return 'False'
							elif obj[10]>18:
								return 'True'
							else: return 'True'
						elif obj[16]>0:
							return 'False'
						else: return 'False'
					elif obj[14]<=0.0:
						return 'True'
					else: return 'True'
				elif obj[12]>3.0:
					return 'True'
				else: return 'True'
			elif obj[11]>5:
				# {"feature": "Bar", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[12]<=2.0:
					return 'True'
				elif obj[12]>2.0:
					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]>1:
						return 'True'
					elif obj[0]<=1:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		elif obj[6]>5:
			return 'False'
		else: return 'False'
	elif obj[3]<=1:
		# {"feature": "Age", "instances": 12, "metric_value": 0.4138, "depth": 2}
		if obj[6]<=5:
			return 'False'
		elif obj[6]>5:
			return 'True'
		else: return 'True'
	else: return 'False'
