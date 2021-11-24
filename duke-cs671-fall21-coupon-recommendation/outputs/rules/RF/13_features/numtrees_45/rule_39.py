def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[2]>0:
		# {"feature": "Passanger", "instances": 19, "metric_value": 0.8997, "depth": 2}
		if obj[0]>0:
			# {"feature": "Time", "instances": 17, "metric_value": 0.7871, "depth": 3}
			if obj[1]>0:
				# {"feature": "Bar", "instances": 12, "metric_value": 0.4138, "depth": 4}
				if obj[8]<=3.0:
					return 'True'
				elif obj[8]>3.0:
					# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[3]<=0:
						# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[11]<=0:
							return 'True'
						elif obj[11]>0:
							return 'False'
						else: return 'False'
					elif obj[3]>0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[1]<=0:
				# {"feature": "Age", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[4]<=1:
					return 'False'
				elif obj[4]>1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[0]<=0:
			return 'False'
		else: return 'False'
	elif obj[2]<=0:
		return 'False'
	else: return 'False'
