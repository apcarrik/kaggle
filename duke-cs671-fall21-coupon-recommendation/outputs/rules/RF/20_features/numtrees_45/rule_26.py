def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Bar", "instances": 23, "metric_value": 0.8865, "depth": 1}
	if obj[14]>0.0:
		# {"feature": "Coupon", "instances": 15, "metric_value": 0.9968, "depth": 2}
		if obj[5]<=3:
			# {"feature": "Age", "instances": 12, "metric_value": 0.9183, "depth": 3}
			if obj[8]<=4:
				# {"feature": "Coupon_validity", "instances": 11, "metric_value": 0.8454, "depth": 4}
				if obj[6]>0:
					# {"feature": "Time", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[4]<=3:
						# {"feature": "Income", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[13]>1:
							return 'True'
						elif obj[13]<=1:
							return 'False'
						else: return 'False'
					elif obj[4]>3:
						return 'False'
					else: return 'False'
				elif obj[6]<=0:
					return 'True'
				else: return 'True'
			elif obj[8]>4:
				return 'False'
			else: return 'False'
		elif obj[5]>3:
			return 'False'
		else: return 'False'
	elif obj[14]<=0.0:
		return 'True'
	else: return 'True'
