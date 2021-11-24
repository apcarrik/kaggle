def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Passanger", "instances": 51, "metric_value": 0.9931, "depth": 1}
	if obj[1]<=2:
		# {"feature": "Temperature", "instances": 39, "metric_value": 0.9881, "depth": 2}
		if obj[3]>30:
			# {"feature": "Education", "instances": 28, "metric_value": 0.9852, "depth": 3}
			if obj[11]>0:
				# {"feature": "Occupation", "instances": 22, "metric_value": 0.994, "depth": 4}
				if obj[12]<=10:
					# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.9183, "depth": 5}
					if obj[17]<=1.0:
						# {"feature": "Gender", "instances": 13, "metric_value": 0.6194, "depth": 6}
						if obj[7]>0:
							return 'False'
						elif obj[7]<=0:
							# {"feature": "Driving_to", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[8]<=2:
									return 'True'
								elif obj[8]>2:
									return 'False'
								else: return 'False'
							elif obj[0]>1:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[17]>1.0:
						# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[8]>1:
							return 'True'
						elif obj[8]<=1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[12]>10:
					return 'True'
				else: return 'True'
			elif obj[11]<=0:
				return 'True'
			else: return 'True'
		elif obj[3]<=30:
			# {"feature": "Time", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[4]>0:
				return 'False'
			elif obj[4]<=0:
				# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0]<=0:
					return 'False'
				elif obj[0]>0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'False'
	elif obj[1]>2:
		# {"feature": "Maritalstatus", "instances": 12, "metric_value": 0.4138, "depth": 2}
		if obj[9]<=1:
			return 'True'
		elif obj[9]>1:
			# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[5]<=3:
				return 'True'
			elif obj[5]>3:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
