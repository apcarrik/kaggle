def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Coupon", "instances": 41, "metric_value": 0.9996, "depth": 1}
	if obj[5]>1:
		# {"feature": "Maritalstatus", "instances": 33, "metric_value": 0.9673, "depth": 2}
		if obj[9]<=1:
			# {"feature": "Time", "instances": 27, "metric_value": 0.999, "depth": 3}
			if obj[4]>1:
				# {"feature": "Education", "instances": 16, "metric_value": 0.896, "depth": 4}
				if obj[11]<=3:
					# {"feature": "Occupation", "instances": 11, "metric_value": 0.994, "depth": 5}
					if obj[12]<=18:
						# {"feature": "Bar", "instances": 9, "metric_value": 0.9183, "depth": 6}
						if obj[14]<=1.0:
							# {"feature": "Temperature", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[3]<=55:
								# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[8]<=3:
									return 'True'
								elif obj[8]>3:
									return 'False'
								else: return 'False'
							elif obj[3]>55:
								return 'False'
							else: return 'False'
						elif obj[14]>1.0:
							return 'True'
						else: return 'True'
					elif obj[12]>18:
						return 'False'
					else: return 'False'
				elif obj[11]>3:
					return 'True'
				else: return 'True'
			elif obj[4]<=1:
				# {"feature": "Age", "instances": 11, "metric_value": 0.8454, "depth": 4}
				if obj[8]>1:
					return 'False'
				elif obj[8]<=1:
					# {"feature": "Temperature", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[3]>30:
						return 'True'
					elif obj[3]<=30:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		elif obj[9]>1:
			return 'True'
		else: return 'True'
	elif obj[5]<=1:
		return 'False'
	else: return 'False'
