def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Education", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[6]<=2:
		# {"feature": "Age", "instances": 27, "metric_value": 0.9183, "depth": 2}
		if obj[4]>2:
			# {"feature": "Coupon", "instances": 18, "metric_value": 0.65, "depth": 3}
			if obj[2]>0:
				# {"feature": "Occupation", "instances": 15, "metric_value": 0.3534, "depth": 4}
				if obj[7]<=10:
					return 'True'
				elif obj[7]>10:
					# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[3]>0:
						return 'False'
					elif obj[3]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[2]<=0:
				# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[1]<=1:
					return 'False'
				elif obj[1]>1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[4]<=2:
			# {"feature": "Occupation", "instances": 9, "metric_value": 0.9183, "depth": 3}
			if obj[7]>6:
				return 'False'
			elif obj[7]<=6:
				# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[2]>1:
					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]>1:
						return 'True'
					elif obj[0]<=1:
						return 'False'
					else: return 'False'
				elif obj[2]<=1:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[6]>2:
		return 'False'
	else: return 'False'
