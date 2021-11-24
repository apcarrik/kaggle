def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Education", "instances": 34, "metric_value": 0.9367, "depth": 1}
	if obj[9]>1:
		# {"feature": "Passanger", "instances": 26, "metric_value": 0.9957, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Distance", "instances": 16, "metric_value": 0.896, "depth": 3}
			if obj[17]<=1:
				# {"feature": "Gender", "instances": 10, "metric_value": 1.0, "depth": 4}
				if obj[5]>0:
					# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[2]<=1:
						return 'True'
					elif obj[2]>1:
						return 'False'
					else: return 'False'
				elif obj[5]<=0:
					# {"feature": "Bar", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[12]<=2.0:
						return 'False'
					elif obj[12]>2.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[17]>1:
				return 'False'
			else: return 'False'
		elif obj[0]>2:
			# {"feature": "Time", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[2]>0:
				return 'True'
			elif obj[2]<=0:
				# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[4]<=0:
					return 'True'
				elif obj[4]>0:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[9]<=1:
		return 'True'
	else: return 'True'
