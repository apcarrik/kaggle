def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[3]<=3:
		# {"feature": "Time", "instances": 14, "metric_value": 0.5917, "depth": 2}
		if obj[2]<=2:
			return 'True'
		elif obj[2]>2:
			# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[17]>1:
				return 'True'
			elif obj[17]<=1:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[3]>3:
		# {"feature": "Education", "instances": 9, "metric_value": 0.9183, "depth": 2}
		if obj[9]>1:
			return 'False'
		elif obj[9]<=1:
			# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[0]>0:
				return 'True'
			elif obj[0]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
