def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Income", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[9]>2:
		# {"feature": "Occupation", "instances": 14, "metric_value": 0.7496, "depth": 2}
		if obj[8]>3:
			# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[11]>0.0:
				return 'False'
			elif obj[11]<=0.0:
				return 'True'
			else: return 'True'
		elif obj[8]<=3:
			# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[0]<=2:
				return 'True'
			elif obj[0]>2:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[9]<=2:
		# {"feature": "Direction_same", "instances": 9, "metric_value": 0.7642, "depth": 2}
		if obj[13]<=0:
			return 'True'
		elif obj[13]>0:
			# {"feature": "Coupon_validity", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[3]>0:
				return 'True'
			elif obj[3]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
