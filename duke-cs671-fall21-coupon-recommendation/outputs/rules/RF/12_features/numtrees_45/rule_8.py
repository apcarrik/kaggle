def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Distance", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[11]<=2:
		# {"feature": "Time", "instances": 19, "metric_value": 0.8997, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Age", "instances": 14, "metric_value": 0.9852, "depth": 3}
			if obj[4]>1:
				# {"feature": "Direction_same", "instances": 9, "metric_value": 0.7642, "depth": 4}
				if obj[10]<=0:
					return 'True'
				elif obj[10]>0:
					# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2]>3:
						return 'False'
					elif obj[2]<=3:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[4]<=1:
				# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[5]<=3:
					return 'False'
				elif obj[5]>3:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	elif obj[11]>2:
		return 'False'
	else: return 'False'
