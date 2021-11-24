def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[15]>0.0:
		# {"feature": "Coffeehouse", "instances": 20, "metric_value": 0.9341, "depth": 2}
		if obj[13]>0.0:
			# {"feature": "Age", "instances": 13, "metric_value": 0.6194, "depth": 3}
			if obj[6]<=3:
				return 'True'
			elif obj[6]>3:
				# {"feature": "Gender", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[5]>0:
					return 'False'
				elif obj[5]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[13]<=0.0:
			# {"feature": "Distance", "instances": 7, "metric_value": 0.8631, "depth": 3}
			if obj[17]<=1:
				return 'False'
			elif obj[17]>1:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[15]<=0.0:
		return 'False'
	else: return 'False'
