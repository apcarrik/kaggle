def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Distance", "instances": 51, "metric_value": 0.9526, "depth": 1}
	if obj[15]<=2:
		# {"feature": "Passanger", "instances": 42, "metric_value": 0.8296, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Occupation", "instances": 30, "metric_value": 0.9183, "depth": 3}
			if obj[9]>2:
				# {"feature": "Time", "instances": 24, "metric_value": 0.9799, "depth": 4}
				if obj[2]>0:
					# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.874, "depth": 5}
					if obj[13]>0.0:
						# {"feature": "Education", "instances": 15, "metric_value": 0.7219, "depth": 6}
						if obj[8]>0:
							# {"feature": "Bar", "instances": 10, "metric_value": 0.8813, "depth": 7}
							if obj[11]<=2.0:
								# {"feature": "Weather", "instances": 8, "metric_value": 0.9544, "depth": 8}
								if obj[1]<=0:
									# {"feature": "Age", "instances": 7, "metric_value": 0.9852, "depth": 9}
									if obj[6]>0:
										# {"feature": "Coupon", "instances": 6, "metric_value": 1.0, "depth": 10}
										if obj[3]>1:
											# {"feature": "Income", "instances": 5, "metric_value": 0.971, "depth": 11}
											if obj[10]<=6:
												# {"feature": "Coffeehouse", "instances": 4, "metric_value": 1.0, "depth": 12}
												if obj[12]>0.0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[14]<=0:
														return 'False'
													elif obj[14]>0:
														return 'True'
													else: return 'True'
												elif obj[12]<=0.0:
													return 'True'
												else: return 'True'
											elif obj[10]>6:
												return 'True'
											else: return 'True'
										elif obj[3]<=1:
											return 'False'
										else: return 'False'
									elif obj[6]<=0:
										return 'True'
									else: return 'True'
								elif obj[1]>0:
									return 'True'
								else: return 'True'
							elif obj[11]>2.0:
								return 'True'
							else: return 'True'
						elif obj[8]<=0:
							return 'True'
						else: return 'True'
					elif obj[13]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[2]<=0:
					# {"feature": "Weather", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[1]<=1:
						return 'False'
					elif obj[1]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[9]<=2:
				return 'True'
			else: return 'True'
		elif obj[0]>2:
			# {"feature": "Occupation", "instances": 12, "metric_value": 0.4138, "depth": 3}
			if obj[9]>2:
				return 'True'
			elif obj[9]<=2:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[15]>2:
		# {"feature": "Occupation", "instances": 9, "metric_value": 0.5033, "depth": 2}
		if obj[9]>1:
			return 'False'
		elif obj[9]<=1:
			return 'True'
		else: return 'True'
	else: return 'False'
