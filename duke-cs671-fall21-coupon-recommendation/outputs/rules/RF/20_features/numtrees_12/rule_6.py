def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Restaurantlessthan20", "instances": 85, "metric_value": 0.971, "depth": 1}
	if obj[16]<=2.0:
		# {"feature": "Education", "instances": 52, "metric_value": 0.8667, "depth": 2}
		if obj[11]<=3:
			# {"feature": "Income", "instances": 47, "metric_value": 0.9035, "depth": 3}
			if obj[13]>0:
				# {"feature": "Age", "instances": 42, "metric_value": 0.9403, "depth": 4}
				if obj[8]>1:
					# {"feature": "Restaurant20to50", "instances": 32, "metric_value": 0.8571, "depth": 5}
					if obj[17]<=1.0:
						# {"feature": "Temperature", "instances": 28, "metric_value": 0.9059, "depth": 6}
						if obj[3]<=55:
							# {"feature": "Coupon", "instances": 16, "metric_value": 0.6962, "depth": 7}
							if obj[5]<=2:
								# {"feature": "Distance", "instances": 9, "metric_value": 0.9183, "depth": 8}
								if obj[19]>1:
									# {"feature": "Weather", "instances": 6, "metric_value": 1.0, "depth": 9}
									if obj[2]<=1:
										# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[12]<=5:
											# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[14]<=1.0:
												return 'False'
											elif obj[14]>1.0:
												return 'True'
											else: return 'True'
										elif obj[12]>5:
											return 'True'
										else: return 'True'
									elif obj[2]>1:
										return 'False'
									else: return 'False'
								elif obj[19]<=1:
									return 'True'
								else: return 'True'
							elif obj[5]>2:
								return 'True'
							else: return 'True'
						elif obj[3]>55:
							# {"feature": "Coupon_validity", "instances": 12, "metric_value": 1.0, "depth": 7}
							if obj[6]<=0:
								# {"feature": "Occupation", "instances": 7, "metric_value": 0.8631, "depth": 8}
								if obj[12]<=11:
									# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 9}
									if obj[1]<=1:
										return 'True'
									elif obj[1]>1:
										# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[9]<=0:
											return 'True'
										elif obj[9]>0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[12]>11:
									return 'False'
								else: return 'False'
							elif obj[6]>0:
								# {"feature": "Maritalstatus", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[9]<=1:
									return 'False'
								elif obj[9]>1:
									return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'False'
					elif obj[17]>1.0:
						return 'True'
					else: return 'True'
				elif obj[8]<=1:
					# {"feature": "Coupon", "instances": 10, "metric_value": 0.971, "depth": 5}
					if obj[5]>0:
						# {"feature": "Driving_to", "instances": 8, "metric_value": 1.0, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Passanger", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[1]>1:
								# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[12]>1:
									# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[17]>1.0:
										return 'True'
									elif obj[17]<=1.0:
										return 'False'
									else: return 'False'
								elif obj[12]<=1:
									return 'False'
								else: return 'False'
							elif obj[1]<=1:
								return 'False'
							else: return 'False'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					elif obj[5]<=0:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[13]<=0:
				return 'True'
			else: return 'True'
		elif obj[11]>3:
			return 'True'
		else: return 'True'
	elif obj[16]>2.0:
		# {"feature": "Coupon_validity", "instances": 33, "metric_value": 0.9834, "depth": 2}
		if obj[6]<=0:
			# {"feature": "Bar", "instances": 21, "metric_value": 0.9852, "depth": 3}
			if obj[14]<=1.0:
				# {"feature": "Coupon", "instances": 14, "metric_value": 0.9403, "depth": 4}
				if obj[5]>1:
					# {"feature": "Education", "instances": 8, "metric_value": 0.9544, "depth": 5}
					if obj[11]>0:
						return 'True'
					elif obj[11]<=0:
						# {"feature": "Driving_to", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[0]>0:
							return 'False'
						elif obj[0]<=0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[5]<=1:
					return 'False'
				else: return 'False'
			elif obj[14]>1.0:
				return 'True'
			else: return 'True'
		elif obj[6]>0:
			# {"feature": "Age", "instances": 12, "metric_value": 0.65, "depth": 3}
			if obj[8]>0:
				# {"feature": "Occupation", "instances": 11, "metric_value": 0.4395, "depth": 4}
				if obj[12]<=16:
					return 'False'
				elif obj[12]>16:
					# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[2]>0:
						return 'False'
					elif obj[2]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[8]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
