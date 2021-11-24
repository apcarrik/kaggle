def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[3]<=3:
		# {"feature": "Time", "instances": 18, "metric_value": 0.7642, "depth": 2}
		if obj[2]<=2:
			return 'True'
		elif obj[2]>2:
			# {"feature": "Distance", "instances": 8, "metric_value": 1.0, "depth": 3}
			if obj[17]>1:
				# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[6]>0:
					return 'True'
				elif obj[6]<=0:
					return 'False'
				else: return 'False'
			elif obj[17]<=1:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[3]>3:
		# {"feature": "Restaurantlessthan20", "instances": 16, "metric_value": 0.9887, "depth": 2}
		if obj[14]<=2.0:
			# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[15]>0.0:
				return 'False'
			elif obj[15]<=0.0:
				# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0]>1:
					return 'True'
				elif obj[0]<=1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[14]>2.0:
			# {"feature": "Time", "instances": 8, "metric_value": 0.8113, "depth": 3}
			if obj[2]<=1:
				# {"feature": "Coupon_validity", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[4]<=0:
					return 'True'
				elif obj[4]>0:
					return 'False'
				else: return 'False'
			elif obj[2]>1:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
