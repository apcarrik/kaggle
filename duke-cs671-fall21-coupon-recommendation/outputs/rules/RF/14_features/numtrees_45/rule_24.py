def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Distance", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[13]>1:
		# {"feature": "Age", "instances": 14, "metric_value": 0.9852, "depth": 2}
		if obj[4]>2:
			# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.9544, "depth": 3}
			if obj[10]<=3.0:
				# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[2]>0:
					# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1]<=2:
						return 'True'
					elif obj[1]>2:
						return 'False'
					else: return 'False'
				elif obj[2]<=0:
					return 'False'
				else: return 'False'
			elif obj[10]>3.0:
				return 'True'
			else: return 'True'
		elif obj[4]<=2:
			# {"feature": "Occupation", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[7]<=7:
				return 'False'
			elif obj[7]>7:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[13]<=1:
		return 'True'
	else: return 'True'
