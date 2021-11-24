def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Distance", "instances": 17, "metric_value": 0.9975, "depth": 2}
		if obj[12]<=2:
			# {"feature": "Time", "instances": 11, "metric_value": 0.8454, "depth": 3}
			if obj[1]<=1:
				# {"feature": "Occupation", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[7]>6:
					return 'True'
				elif obj[7]<=6:
					return 'False'
				else: return 'False'
			elif obj[1]>1:
				return 'False'
			else: return 'False'
		elif obj[12]>2:
			# {"feature": "Bar", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[8]<=2.0:
				return 'True'
			elif obj[8]>2.0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[0]>1:
		return 'True'
	else: return 'True'
