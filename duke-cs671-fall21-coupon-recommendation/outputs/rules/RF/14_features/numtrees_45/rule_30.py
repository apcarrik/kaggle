def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Education", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[6]<=3:
		# {"feature": "Gender", "instances": 19, "metric_value": 0.998, "depth": 2}
		if obj[3]<=0:
			# {"feature": "Time", "instances": 10, "metric_value": 0.8813, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Coupon", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[2]>3:
					# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[4]<=2:
						return 'False'
					elif obj[4]>2:
						return 'True'
					else: return 'True'
				elif obj[2]<=3:
					return 'True'
				else: return 'True'
			elif obj[1]>3:
				return 'False'
			else: return 'False'
		elif obj[3]>0:
			# {"feature": "Distance", "instances": 9, "metric_value": 0.7642, "depth": 3}
			if obj[13]<=1:
				return 'True'
			elif obj[13]>1:
				# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[0]<=1:
					return 'False'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[6]>3:
		return 'True'
	else: return 'True'
