def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Age", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[6]>1:
		# {"feature": "Passanger", "instances": 13, "metric_value": 0.6194, "depth": 2}
		if obj[0]>0:
			return 'False'
		elif obj[0]<=0:
			# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[8]<=0:
				return 'True'
			elif obj[8]>0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[6]<=1:
		# {"feature": "Gender", "instances": 10, "metric_value": 0.7219, "depth": 2}
		if obj[5]>0:
			return 'True'
		elif obj[5]<=0:
			# {"feature": "Coupon_validity", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[4]>0:
				return 'False'
			elif obj[4]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
