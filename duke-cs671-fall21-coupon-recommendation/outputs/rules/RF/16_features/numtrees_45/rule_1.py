def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Education", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[8]>0:
		# {"feature": "Income", "instances": 13, "metric_value": 0.9612, "depth": 2}
		if obj[10]>3:
			# {"feature": "Coupon", "instances": 8, "metric_value": 0.9544, "depth": 3}
			if obj[3]>0:
				# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[0]>0:
					return 'True'
				elif obj[0]<=0:
					return 'False'
				else: return 'False'
			elif obj[3]<=0:
				return 'False'
			else: return 'False'
		elif obj[10]<=3:
			return 'False'
		else: return 'False'
	elif obj[8]<=0:
		# {"feature": "Coupon", "instances": 10, "metric_value": 0.469, "depth": 2}
		if obj[3]>0:
			return 'True'
		elif obj[3]<=0:
			return 'False'
		else: return 'False'
	else: return 'True'
