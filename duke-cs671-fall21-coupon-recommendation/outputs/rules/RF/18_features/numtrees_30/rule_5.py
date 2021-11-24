def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Coffeehouse", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[13]>0.0:
		# {"feature": "Distance", "instances": 29, "metric_value": 0.9576, "depth": 2}
		if obj[17]<=2:
			# {"feature": "Coupon_validity", "instances": 25, "metric_value": 0.8555, "depth": 3}
			if obj[4]<=0:
				# {"feature": "Coupon", "instances": 13, "metric_value": 0.3912, "depth": 4}
				if obj[3]>1:
					return 'True'
				elif obj[3]<=1:
					return 'False'
				else: return 'False'
			elif obj[4]>0:
				# {"feature": "Time", "instances": 12, "metric_value": 1.0, "depth": 4}
				if obj[2]<=2:
					# {"feature": "Children", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[8]<=0:
						return 'False'
					elif obj[8]>0:
						return 'True'
					else: return 'True'
				elif obj[2]>2:
					# {"feature": "Maritalstatus", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[7]<=1:
						return 'True'
					elif obj[7]>1:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		elif obj[17]>2:
			return 'False'
		else: return 'False'
	elif obj[13]<=0.0:
		return 'False'
	else: return 'False'
