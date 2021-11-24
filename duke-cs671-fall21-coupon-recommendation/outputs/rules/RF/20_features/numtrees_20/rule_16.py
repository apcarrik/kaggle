def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Restaurant20to50", "instances": 51, "metric_value": 0.9931, "depth": 1}
	if obj[17]<=2.0:
		# {"feature": "Bar", "instances": 45, "metric_value": 0.9996, "depth": 2}
		if obj[14]>0.0:
			# {"feature": "Restaurantlessthan20", "instances": 31, "metric_value": 0.9383, "depth": 3}
			if obj[16]<=2.0:
				# {"feature": "Time", "instances": 16, "metric_value": 0.5436, "depth": 4}
				if obj[4]>0:
					return 'False'
				elif obj[4]<=0:
					# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[11]<=0:
						return 'False'
					elif obj[11]>0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[16]>2.0:
				# {"feature": "Education", "instances": 15, "metric_value": 0.971, "depth": 4}
				if obj[11]>0:
					# {"feature": "Time", "instances": 9, "metric_value": 0.9183, "depth": 5}
					if obj[4]<=2:
						# {"feature": "Temperature", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[3]<=55:
							# {"feature": "Coupon_validity", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[6]<=0:
								return 'False'
							elif obj[6]>0:
								return 'True'
							else: return 'True'
						elif obj[3]>55:
							return 'True'
						else: return 'True'
					elif obj[4]>2:
						return 'False'
					else: return 'False'
				elif obj[11]<=0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[14]<=0.0:
			# {"feature": "Coupon", "instances": 14, "metric_value": 0.7496, "depth": 3}
			if obj[5]>1:
				return 'True'
			elif obj[5]<=1:
				# {"feature": "Age", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[8]>1:
					return 'False'
				elif obj[8]<=1:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[17]>2.0:
		return 'True'
	else: return 'True'
