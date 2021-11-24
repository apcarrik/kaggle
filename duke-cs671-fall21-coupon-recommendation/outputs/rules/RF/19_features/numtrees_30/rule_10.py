def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Education", "instances": 34, "metric_value": 0.9367, "depth": 1}
	if obj[10]<=2:
		# {"feature": "Passanger", "instances": 29, "metric_value": 0.7973, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Bar", "instances": 15, "metric_value": 0.971, "depth": 3}
			if obj[13]>0.0:
				# {"feature": "Age", "instances": 9, "metric_value": 0.9183, "depth": 4}
				if obj[7]>3:
					# {"feature": "Temperature", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[2]>55:
						# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[3]<=3:
							return 'False'
						elif obj[3]>3:
							return 'True'
						else: return 'True'
					elif obj[2]<=55:
						return 'True'
					else: return 'True'
				elif obj[7]<=3:
					return 'False'
				else: return 'False'
			elif obj[13]<=0.0:
				return 'True'
			else: return 'True'
		elif obj[0]>2:
			# {"feature": "Occupation", "instances": 14, "metric_value": 0.3712, "depth": 3}
			if obj[11]<=7:
				return 'True'
			elif obj[11]>7:
				# {"feature": "Temperature", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[2]<=55:
					return 'True'
				elif obj[2]>55:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[10]>2:
		return 'False'
	else: return 'False'
