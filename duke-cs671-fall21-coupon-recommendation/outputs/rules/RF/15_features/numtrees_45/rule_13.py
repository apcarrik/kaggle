def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Children", "instances": 23, "metric_value": 0.8865, "depth": 1}
	if obj[6]<=0:
		# {"feature": "Coffeehouse", "instances": 15, "metric_value": 0.3534, "depth": 2}
		if obj[11]<=2.0:
			return 'True'
		elif obj[11]>2.0:
			# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[1]<=1:
				return 'False'
			elif obj[1]>1:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[6]>0:
		# {"feature": "Bar", "instances": 8, "metric_value": 0.8113, "depth": 2}
		if obj[10]<=0.0:
			return 'False'
		elif obj[10]>0.0:
			# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[0]>1:
				return 'True'
			elif obj[0]<=1:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
