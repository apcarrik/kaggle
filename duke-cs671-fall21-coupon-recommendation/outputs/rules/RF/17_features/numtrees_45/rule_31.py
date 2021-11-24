def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Coffeehouse", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[13]>1.0:
		# {"feature": "Income", "instances": 13, "metric_value": 0.7793, "depth": 2}
		if obj[11]>1:
			# {"feature": "Maritalstatus", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[7]>0:
				return 'True'
			elif obj[7]<=0:
				# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[16]<=1:
					return 'True'
				elif obj[16]>1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[11]<=1:
			return 'False'
		else: return 'False'
	elif obj[13]<=1.0:
		# {"feature": "Education", "instances": 10, "metric_value": 0.8813, "depth": 2}
		if obj[9]<=1:
			# {"feature": "Children", "instances": 6, "metric_value": 1.0, "depth": 3}
			if obj[8]>0:
				# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[3]>3:
					return 'False'
				elif obj[3]<=3:
					return 'True'
				else: return 'True'
			elif obj[8]<=0:
				return 'True'
			else: return 'True'
		elif obj[9]>1:
			return 'False'
		else: return 'False'
	else: return 'False'
