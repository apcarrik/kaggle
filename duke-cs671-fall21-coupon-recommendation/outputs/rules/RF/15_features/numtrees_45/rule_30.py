def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.9968, "depth": 2}
		if obj[12]<=1.0:
			# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.8113, "depth": 3}
			if obj[11]>0.0:
				return 'True'
			elif obj[11]<=0.0:
				return 'False'
			else: return 'False'
		elif obj[12]>1.0:
			# {"feature": "Time", "instances": 7, "metric_value": 0.5917, "depth": 3}
			if obj[1]<=3:
				return 'False'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[0]>1:
		return 'True'
	else: return 'True'
