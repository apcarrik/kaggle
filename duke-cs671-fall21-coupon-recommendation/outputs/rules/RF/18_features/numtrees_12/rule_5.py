def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.874, "depth": 1}
	if obj[3]<=3:
		# {"feature": "Occupation", "instances": 58, "metric_value": 0.7355, "depth": 2}
		if obj[10]<=20:
			# {"feature": "Coffeehouse", "instances": 56, "metric_value": 0.6769, "depth": 3}
			if obj[13]>0.0:
				# {"feature": "Time", "instances": 45, "metric_value": 0.7642, "depth": 4}
				if obj[2]<=3:
					# {"feature": "Bar", "instances": 39, "metric_value": 0.8213, "depth": 5}
					if obj[12]<=3.0:
						# {"feature": "Distance", "instances": 38, "metric_value": 0.7897, "depth": 6}
						if obj[17]>1:
							# {"feature": "Restaurantlessthan20", "instances": 24, "metric_value": 0.9183, "depth": 7}
							if obj[14]<=2.0:
								# {"feature": "Age", "instances": 15, "metric_value": 0.9968, "depth": 8}
								if obj[6]<=4:
									# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.9612, "depth": 9}
									if obj[15]>-1.0:
										# {"feature": "Weather", "instances": 11, "metric_value": 0.994, "depth": 10}
										if obj[1]<=1:
											# {"feature": "Passanger", "instances": 10, "metric_value": 1.0, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Maritalstatus", "instances": 6, "metric_value": 0.9183, "depth": 12}
												if obj[7]>0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 13}
													if obj[16]<=0:
														return 'False'
													elif obj[16]>0:
														return 'True'
													else: return 'True'
												elif obj[7]<=0:
													return 'True'
												else: return 'True'
											elif obj[0]>1:
												# {"feature": "Coupon_validity", "instances": 4, "metric_value": 0.8113, "depth": 12}
												if obj[4]>0:
													return 'True'
												elif obj[4]<=0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[1]>1:
											return 'True'
										else: return 'True'
									elif obj[15]<=-1.0:
										return 'True'
									else: return 'True'
								elif obj[6]>4:
									return 'False'
								else: return 'False'
							elif obj[14]>2.0:
								# {"feature": "Income", "instances": 9, "metric_value": 0.5033, "depth": 8}
								if obj[11]<=6:
									return 'True'
								elif obj[11]>6:
									# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[0]<=1:
										return 'True'
									elif obj[0]>1:
										return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'True'
						elif obj[17]<=1:
							# {"feature": "Education", "instances": 14, "metric_value": 0.3712, "depth": 7}
							if obj[9]<=2:
								return 'True'
							elif obj[9]>2:
								# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[6]>1:
									return 'True'
								elif obj[6]<=1:
									return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					elif obj[12]>3.0:
						return 'False'
					else: return 'False'
				elif obj[2]>3:
					return 'True'
				else: return 'True'
			elif obj[13]<=0.0:
				return 'True'
			else: return 'True'
		elif obj[10]>20:
			return 'False'
		else: return 'False'
	elif obj[3]>3:
		# {"feature": "Coffeehouse", "instances": 27, "metric_value": 0.999, "depth": 2}
		if obj[13]>0.0:
			# {"feature": "Bar", "instances": 19, "metric_value": 0.9495, "depth": 3}
			if obj[12]>0.0:
				# {"feature": "Income", "instances": 14, "metric_value": 1.0, "depth": 4}
				if obj[11]<=4:
					# {"feature": "Education", "instances": 11, "metric_value": 0.9457, "depth": 5}
					if obj[9]<=2:
						# {"feature": "Distance", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[17]<=1:
							return 'True'
						elif obj[17]>1:
							return 'False'
						else: return 'False'
					elif obj[9]>2:
						return 'False'
					else: return 'False'
				elif obj[11]>4:
					return 'True'
				else: return 'True'
			elif obj[12]<=0.0:
				return 'True'
			else: return 'True'
		elif obj[13]<=0.0:
			# {"feature": "Passanger", "instances": 8, "metric_value": 0.8113, "depth": 3}
			if obj[0]>1:
				# {"feature": "Education", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[9]>0:
					return 'True'
				elif obj[9]<=0:
					return 'False'
				else: return 'False'
			elif obj[0]<=1:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'True'
