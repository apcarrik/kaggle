def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Time", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[1]<=2:
		# {"feature": "Coupon", "instances": 17, "metric_value": 0.9975, "depth": 2}
		if obj[2]<=3:
			# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.8813, "depth": 3}
			if obj[10]>0.0:
				# {"feature": "Gender", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[3]<=0:
					return 'True'
				elif obj[3]>0:
					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]<=1:
						return 'True'
					elif obj[0]>1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[10]<=0.0:
				return 'False'
			else: return 'False'
		elif obj[2]>3:
			# {"feature": "Age", "instances": 7, "metric_value": 0.5917, "depth": 3}
			if obj[4]>0:
				return 'False'
			elif obj[4]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[1]>2:
		return 'False'
	else: return 'False'
