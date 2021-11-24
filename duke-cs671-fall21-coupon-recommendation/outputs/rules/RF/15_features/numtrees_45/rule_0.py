def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Children", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[6]<=0:
		# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.4138, "depth": 2}
		if obj[12]<=2.0:
			return 'True'
		elif obj[12]>2.0:
			return 'False'
		else: return 'False'
	elif obj[6]>0:
		# {"feature": "Distance", "instances": 11, "metric_value": 0.9457, "depth": 2}
		if obj[14]>2:
			# {"feature": "Gender", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[4]>0:
				# {"feature": "Income", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[9]>3:
					# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[7]>1:
						return 'True'
					elif obj[7]<=1:
						return 'False'
					else: return 'False'
				elif obj[9]<=3:
					return 'False'
				else: return 'False'
			elif obj[4]<=0:
				return 'True'
			else: return 'True'
		elif obj[14]<=2:
			return 'False'
		else: return 'False'
	else: return 'False'
