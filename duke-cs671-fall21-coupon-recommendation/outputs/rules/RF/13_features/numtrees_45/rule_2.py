def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Time", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[1]>0:
		# {"feature": "Coupon", "instances": 17, "metric_value": 0.9774, "depth": 2}
		if obj[2]>0:
			# {"feature": "Occupation", "instances": 12, "metric_value": 0.8113, "depth": 3}
			if obj[7]<=10:
				return 'True'
			elif obj[7]>10:
				# {"feature": "Age", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[4]>1:
					# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[6]<=1:
						return 'False'
					elif obj[6]>1:
						return 'True'
					else: return 'True'
				elif obj[4]<=1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[2]<=0:
			# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[9]>0.0:
				return 'False'
			elif obj[9]<=0.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[1]<=0:
		# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 2}
		if obj[6]>0:
			return 'False'
		elif obj[6]<=0:
			# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[4]<=0:
				return 'False'
			elif obj[4]>0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
