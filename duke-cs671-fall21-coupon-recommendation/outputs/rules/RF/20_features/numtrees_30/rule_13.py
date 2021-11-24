def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[5]>1:
		# {"feature": "Coupon_validity", "instances": 27, "metric_value": 0.8256, "depth": 2}
		if obj[6]<=0:
			# {"feature": "Maritalstatus", "instances": 16, "metric_value": 0.3373, "depth": 3}
			if obj[9]<=2:
				return 'True'
			elif obj[9]>2:
				# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0]<=0:
					return 'True'
				elif obj[0]>0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[6]>0:
			# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.994, "depth": 3}
			if obj[17]<=1.0:
				# {"feature": "Bar", "instances": 9, "metric_value": 0.9183, "depth": 4}
				if obj[14]<=1.0:
					# {"feature": "Children", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[10]>0:
						# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[1]<=1:
							return 'False'
						elif obj[1]>1:
							return 'True'
						else: return 'True'
					elif obj[10]<=0:
						return 'True'
					else: return 'True'
				elif obj[14]>1.0:
					return 'False'
				else: return 'False'
			elif obj[17]>1.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[5]<=1:
		# {"feature": "Age", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[8]>0:
			return 'False'
		elif obj[8]<=0:
			return 'True'
		else: return 'True'
	else: return 'False'
