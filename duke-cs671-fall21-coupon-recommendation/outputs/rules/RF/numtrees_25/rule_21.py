def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Distance", "instances": 41, "metric_value": 0.9961, "depth": 1}
	if obj[20]<=2:
		# {"feature": "Bar", "instances": 33, "metric_value": 0.9834, "depth": 2}
		if obj[14]>0.0:
			# {"feature": "Age", "instances": 21, "metric_value": 0.7919, "depth": 3}
			if obj[8]<=2:
				# {"feature": "Coupon_validity", "instances": 11, "metric_value": 0.994, "depth": 4}
				if obj[6]<=0:
					# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[1]<=1:
						return 'True'
					elif obj[1]>1:
						return 'False'
					else: return 'False'
				elif obj[6]>0:
					# {"feature": "Temperature", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[3]>30:
						return 'False'
					elif obj[3]<=30:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[8]>2:
				return 'True'
			else: return 'True'
		elif obj[14]<=0.0:
			# {"feature": "Gender", "instances": 12, "metric_value": 0.8113, "depth": 3}
			if obj[7]<=0:
				return 'False'
			elif obj[7]>0:
				# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[5]>1:
					return 'True'
				elif obj[5]<=1:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[20]>2:
		return 'False'
	else: return 'False'
