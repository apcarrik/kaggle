def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Distance", "instances": 34, "metric_value": 0.9367, "depth": 1}
	if obj[11]>1:
		# {"feature": "Coupon", "instances": 21, "metric_value": 0.9984, "depth": 2}
		if obj[2]<=3:
			# {"feature": "Passanger", "instances": 15, "metric_value": 0.9183, "depth": 3}
			if obj[0]>2:
				# {"feature": "Age", "instances": 9, "metric_value": 0.5033, "depth": 4}
				if obj[4]<=2:
					return 'True'
				elif obj[4]>2:
					# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[3]>0:
						return 'True'
					elif obj[3]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[0]<=2:
				# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[8]<=2.0:
					return 'False'
				elif obj[8]>2.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[2]>3:
			return 'False'
		else: return 'False'
	elif obj[11]<=1:
		# {"feature": "Age", "instances": 13, "metric_value": 0.3912, "depth": 2}
		if obj[4]<=4:
			return 'True'
		elif obj[4]>4:
			# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[0]>1:
				return 'True'
			elif obj[0]<=1:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
