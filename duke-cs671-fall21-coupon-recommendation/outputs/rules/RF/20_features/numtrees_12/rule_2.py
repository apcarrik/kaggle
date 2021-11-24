def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Education", "instances": 85, "metric_value": 0.9999, "depth": 1}
	if obj[11]<=2:
		# {"feature": "Occupation", "instances": 61, "metric_value": 0.967, "depth": 2}
		if obj[12]<=7:
			# {"feature": "Weather", "instances": 41, "metric_value": 0.839, "depth": 3}
			if obj[2]<=0:
				# {"feature": "Restaurantlessthan20", "instances": 36, "metric_value": 0.888, "depth": 4}
				if obj[16]<=2.0:
					# {"feature": "Age", "instances": 21, "metric_value": 0.9852, "depth": 5}
					if obj[8]<=5:
						# {"feature": "Coupon", "instances": 18, "metric_value": 1.0, "depth": 6}
						if obj[5]>0:
							# {"feature": "Children", "instances": 17, "metric_value": 0.9975, "depth": 7}
							if obj[10]<=0:
								# {"feature": "Direction_same", "instances": 15, "metric_value": 0.9968, "depth": 8}
								if obj[18]<=0:
									# {"feature": "Coupon_validity", "instances": 13, "metric_value": 0.9612, "depth": 9}
									if obj[6]<=0:
										# {"feature": "Time", "instances": 7, "metric_value": 0.9852, "depth": 10}
										if obj[4]>2:
											# {"feature": "Maritalstatus", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[9]<=1:
												return 'False'
											elif obj[9]>1:
												return 'True'
											else: return 'True'
										elif obj[4]<=2:
											return 'True'
										else: return 'True'
									elif obj[6]>0:
										# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 10}
										if obj[4]<=2:
											return 'False'
										elif obj[4]>2:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[18]>0:
									return 'True'
								else: return 'True'
							elif obj[10]>0:
								return 'True'
							else: return 'True'
						elif obj[5]<=0:
							return 'False'
						else: return 'False'
					elif obj[8]>5:
						return 'True'
					else: return 'True'
				elif obj[16]>2.0:
					# {"feature": "Coffeehouse", "instances": 15, "metric_value": 0.5665, "depth": 5}
					if obj[15]<=2.0:
						return 'True'
					elif obj[15]>2.0:
						# {"feature": "Coupon", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[5]<=3:
							return 'False'
						elif obj[5]>3:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[2]>0:
				return 'True'
			else: return 'True'
		elif obj[12]>7:
			# {"feature": "Coffeehouse", "instances": 20, "metric_value": 0.9341, "depth": 3}
			if obj[15]<=2.0:
				# {"feature": "Income", "instances": 15, "metric_value": 0.7219, "depth": 4}
				if obj[13]>2:
					return 'False'
				elif obj[13]<=2:
					# {"feature": "Passanger", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[1]<=2:
						# {"feature": "Coupon_validity", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[6]<=0:
							return 'False'
						elif obj[6]>0:
							return 'True'
						else: return 'True'
					elif obj[1]>2:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[15]>2.0:
				# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[1]<=1:
					return 'True'
				elif obj[1]>1:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[11]>2:
		# {"feature": "Bar", "instances": 24, "metric_value": 0.8113, "depth": 2}
		if obj[14]>0.0:
			# {"feature": "Coffeehouse", "instances": 15, "metric_value": 0.971, "depth": 3}
			if obj[15]>0.0:
				# {"feature": "Age", "instances": 13, "metric_value": 0.8905, "depth": 4}
				if obj[8]>1:
					# {"feature": "Temperature", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[3]>55:
						# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[12]>1:
							return 'False'
						elif obj[12]<=1:
							return 'True'
						else: return 'True'
					elif obj[3]<=55:
						return 'True'
					else: return 'True'
				elif obj[8]<=1:
					return 'False'
				else: return 'False'
			elif obj[15]<=0.0:
				return 'True'
			else: return 'True'
		elif obj[14]<=0.0:
			return 'False'
		else: return 'False'
	else: return 'False'
