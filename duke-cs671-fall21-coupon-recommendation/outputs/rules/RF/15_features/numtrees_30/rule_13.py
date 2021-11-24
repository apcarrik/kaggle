def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Education", "instances": 34, "metric_value": 0.9367, "depth": 1}
	if obj[7]>0:
		# {"feature": "Occupation", "instances": 21, "metric_value": 0.9984, "depth": 2}
		if obj[8]<=11:
			# {"feature": "Bar", "instances": 16, "metric_value": 0.9544, "depth": 3}
			if obj[10]<=2.0:
				# {"feature": "Time", "instances": 12, "metric_value": 0.8113, "depth": 4}
				if obj[1]<=2:
					# {"feature": "Children", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[6]<=0:
						return 'False'
					elif obj[6]>0:
						return 'True'
					else: return 'True'
				elif obj[1]>2:
					return 'False'
				else: return 'False'
			elif obj[10]>2.0:
				# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[1]>0:
					return 'True'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[8]>11:
			return 'True'
		else: return 'True'
	elif obj[7]<=0:
		# {"feature": "Income", "instances": 13, "metric_value": 0.6194, "depth": 2}
		if obj[9]>3:
			return 'True'
		elif obj[9]<=3:
			# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[2]>3:
				# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[5]>0:
					return 'False'
				elif obj[5]<=0:
					return 'True'
				else: return 'True'
			elif obj[2]<=3:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'True'
