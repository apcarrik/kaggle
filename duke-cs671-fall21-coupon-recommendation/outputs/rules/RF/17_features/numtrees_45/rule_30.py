def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[3]>0:
		# {"feature": "Age", "instances": 19, "metric_value": 0.8997, "depth": 2}
		if obj[6]>1:
			# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.994, "depth": 3}
			if obj[14]>0.0:
				# {"feature": "Occupation", "instances": 9, "metric_value": 0.9183, "depth": 4}
				if obj[10]>6:
					# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[16]>1:
						return 'True'
					elif obj[16]<=1:
						return 'False'
					else: return 'False'
				elif obj[10]<=6:
					return 'False'
				else: return 'False'
			elif obj[14]<=0.0:
				return 'True'
			else: return 'True'
		elif obj[6]<=1:
			return 'True'
		else: return 'True'
	elif obj[3]<=0:
		return 'False'
	else: return 'False'
