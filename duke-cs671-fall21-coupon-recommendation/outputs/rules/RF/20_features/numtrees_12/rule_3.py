def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Education", "instances": 85, "metric_value": 0.9774, "depth": 1}
	if obj[11]<=2:
		# {"feature": "Temperature", "instances": 60, "metric_value": 0.9007, "depth": 2}
		if obj[3]>30:
			# {"feature": "Coffeehouse", "instances": 45, "metric_value": 0.9825, "depth": 3}
			if obj[15]>0.0:
				# {"feature": "Age", "instances": 36, "metric_value": 0.9183, "depth": 4}
				if obj[8]>0:
					# {"feature": "Maritalstatus", "instances": 31, "metric_value": 0.8238, "depth": 5}
					if obj[9]<=1:
						# {"feature": "Time", "instances": 21, "metric_value": 0.5917, "depth": 6}
						if obj[4]>1:
							return 'True'
						elif obj[4]<=1:
							# {"feature": "Children", "instances": 10, "metric_value": 0.8813, "depth": 7}
							if obj[10]>0:
								return 'True'
							elif obj[10]<=0:
								# {"feature": "Restaurantlessthan20", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[16]>1.0:
									# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[17]<=2.0:
										return 'False'
									elif obj[17]>2.0:
										return 'True'
									else: return 'True'
								elif obj[16]<=1.0:
									return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'True'
					elif obj[9]>1:
						# {"feature": "Children", "instances": 10, "metric_value": 1.0, "depth": 6}
						if obj[10]<=0:
							# {"feature": "Time", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[4]>1:
								# {"feature": "Driving_to", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[0]<=0:
									# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[5]>0:
										# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[12]>7:
											return 'True'
										elif obj[12]<=7:
											return 'False'
										else: return 'False'
									elif obj[5]<=0:
										return 'True'
									else: return 'True'
								elif obj[0]>0:
									return 'False'
								else: return 'False'
							elif obj[4]<=1:
								return 'True'
							else: return 'True'
						elif obj[10]>0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[8]<=0:
					# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[4]>0:
						return 'False'
					elif obj[4]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[15]<=0.0:
				# {"feature": "Coupon_validity", "instances": 9, "metric_value": 0.7642, "depth": 4}
				if obj[6]<=0:
					return 'False'
				elif obj[6]>0:
					# {"feature": "Income", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[13]>3:
						return 'True'
					elif obj[13]<=3:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		elif obj[3]<=30:
			return 'True'
		else: return 'True'
	elif obj[11]>2:
		# {"feature": "Time", "instances": 25, "metric_value": 0.9427, "depth": 2}
		if obj[4]<=3:
			# {"feature": "Coupon_validity", "instances": 18, "metric_value": 0.7642, "depth": 3}
			if obj[6]<=0:
				# {"feature": "Income", "instances": 10, "metric_value": 0.971, "depth": 4}
				if obj[13]<=3:
					# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[15]>1.0:
						# {"feature": "Driving_to", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[3]<=55:
								return 'False'
							elif obj[3]>55:
								return 'True'
							else: return 'True'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					elif obj[15]<=1.0:
						return 'False'
					else: return 'False'
				elif obj[13]>3:
					return 'True'
				else: return 'True'
			elif obj[6]>0:
				return 'False'
			else: return 'False'
		elif obj[4]>3:
			# {"feature": "Gender", "instances": 7, "metric_value": 0.8631, "depth": 3}
			if obj[7]<=0:
				return 'True'
			elif obj[7]>0:
				# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[1]<=1:
					return 'False'
				elif obj[1]>1:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	else: return 'False'
