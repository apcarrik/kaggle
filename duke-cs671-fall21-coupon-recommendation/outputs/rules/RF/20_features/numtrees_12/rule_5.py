def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.971, "depth": 1}
	if obj[5]>1:
		# {"feature": "Coupon_validity", "instances": 69, "metric_value": 0.8865, "depth": 2}
		if obj[6]>0:
			# {"feature": "Age", "instances": 40, "metric_value": 0.9837, "depth": 3}
			if obj[8]<=5:
				# {"feature": "Maritalstatus", "instances": 34, "metric_value": 1.0, "depth": 4}
				if obj[9]>0:
					# {"feature": "Coffeehouse", "instances": 21, "metric_value": 0.9587, "depth": 5}
					if obj[15]<=3.0:
						# {"feature": "Occupation", "instances": 19, "metric_value": 0.8997, "depth": 6}
						if obj[12]>1:
							# {"feature": "Income", "instances": 16, "metric_value": 0.9544, "depth": 7}
							if obj[13]<=6:
								# {"feature": "Distance", "instances": 14, "metric_value": 0.8631, "depth": 8}
								if obj[19]<=1:
									# {"feature": "Gender", "instances": 10, "metric_value": 0.971, "depth": 9}
									if obj[7]>0:
										# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 10}
										if obj[4]<=2:
											return 'True'
										elif obj[4]>2:
											return 'False'
										else: return 'False'
									elif obj[7]<=0:
										# {"feature": "Temperature", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[3]>30:
											return 'False'
										elif obj[3]<=30:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[19]>1:
									return 'True'
								else: return 'True'
							elif obj[13]>6:
								return 'False'
							else: return 'False'
						elif obj[12]<=1:
							return 'True'
						else: return 'True'
					elif obj[15]>3.0:
						return 'False'
					else: return 'False'
				elif obj[9]<=0:
					# {"feature": "Education", "instances": 13, "metric_value": 0.8905, "depth": 5}
					if obj[11]<=2:
						# {"feature": "Restaurantlessthan20", "instances": 11, "metric_value": 0.684, "depth": 6}
						if obj[16]<=2.0:
							return 'False'
						elif obj[16]>2.0:
							# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[4]<=0:
								return 'True'
							elif obj[4]>0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[11]>2:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[8]>5:
				return 'True'
			else: return 'True'
		elif obj[6]<=0:
			# {"feature": "Gender", "instances": 29, "metric_value": 0.5788, "depth": 3}
			if obj[7]>0:
				return 'True'
			elif obj[7]<=0:
				# {"feature": "Distance", "instances": 14, "metric_value": 0.8631, "depth": 4}
				if obj[19]<=1:
					# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[15]<=1.0:
						return 'False'
					elif obj[15]>1.0:
						return 'True'
					else: return 'True'
				elif obj[19]>1:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[5]<=1:
		# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.6962, "depth": 2}
		if obj[17]<=1.0:
			return 'False'
		elif obj[17]>1.0:
			# {"feature": "Weather", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[2]<=0:
				# {"feature": "Income", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[13]<=5:
					return 'False'
				elif obj[13]>5:
					return 'True'
				else: return 'True'
			elif obj[2]>0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
