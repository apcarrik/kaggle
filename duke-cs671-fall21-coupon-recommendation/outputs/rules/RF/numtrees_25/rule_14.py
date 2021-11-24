def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Time", "instances": 41, "metric_value": 0.9961, "depth": 1}
	if obj[4]<=3:
		# {"feature": "Coffeehouse", "instances": 34, "metric_value": 0.99, "depth": 2}
		if obj[15]>0.0:
			# {"feature": "Income", "instances": 25, "metric_value": 0.9896, "depth": 3}
			if obj[13]>0:
				# {"feature": "Maritalstatus", "instances": 20, "metric_value": 0.9928, "depth": 4}
				if obj[9]<=1:
					# {"feature": "Bar", "instances": 14, "metric_value": 0.8631, "depth": 5}
					if obj[14]>0.0:
						# {"feature": "Temperature", "instances": 10, "metric_value": 0.971, "depth": 6}
						if obj[3]>30:
							# {"feature": "Age", "instances": 8, "metric_value": 1.0, "depth": 7}
							if obj[8]<=4:
								# {"feature": "Children", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[10]<=0:
									# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[1]>0:
										return 'False'
									elif obj[1]<=0:
										return 'True'
									else: return 'True'
								elif obj[10]>0:
									return 'True'
								else: return 'True'
							elif obj[8]>4:
								return 'False'
							else: return 'False'
						elif obj[3]<=30:
							return 'False'
						else: return 'False'
					elif obj[14]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[9]>1:
					# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[1]>0:
						return 'True'
					elif obj[1]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[13]<=0:
				return 'True'
			else: return 'True'
		elif obj[15]<=0.0:
			# {"feature": "Passanger", "instances": 9, "metric_value": 0.5033, "depth": 3}
			if obj[1]<=1:
				return 'False'
			elif obj[1]>1:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[4]>3:
		return 'True'
	else: return 'True'
