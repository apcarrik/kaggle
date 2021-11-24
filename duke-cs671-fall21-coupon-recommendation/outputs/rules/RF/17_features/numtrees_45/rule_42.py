def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Time", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[2]<=1:
		# {"feature": "Bar", "instances": 15, "metric_value": 0.971, "depth": 2}
		if obj[12]<=1.0:
			# {"feature": "Distance", "instances": 12, "metric_value": 0.8113, "depth": 3}
			if obj[16]>1:
				return 'False'
			elif obj[16]<=1:
				# {"feature": "Income", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[11]>2:
					return 'True'
				elif obj[11]<=2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[12]>1.0:
			return 'True'
		else: return 'True'
	elif obj[2]>1:
		return 'True'
	else: return 'True'
