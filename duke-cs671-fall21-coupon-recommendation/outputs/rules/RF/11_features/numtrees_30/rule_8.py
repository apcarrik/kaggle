def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Bar", "instances": 34, "metric_value": 0.9367, "depth": 1}
	if obj[6]<=0.0:
		# {"feature": "Coupon", "instances": 21, "metric_value": 0.9984, "depth": 2}
		if obj[2]<=3:
			# {"feature": "Education", "instances": 15, "metric_value": 0.9183, "depth": 3}
			if obj[4]>0:
				# {"feature": "Occupation", "instances": 10, "metric_value": 1.0, "depth": 4}
				if obj[5]>4:
					# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[3]<=6:
						return 'False'
					elif obj[3]>6:
						return 'True'
					else: return 'True'
				elif obj[5]<=4:
					# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[10]<=2:
						return 'True'
					elif obj[10]>2:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[4]<=0:
				return 'True'
			else: return 'True'
		elif obj[2]>3:
			# {"feature": "Occupation", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[5]<=21:
				return 'False'
			elif obj[5]>21:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[6]>0.0:
		# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.6194, "depth": 2}
		if obj[8]>1.0:
			return 'True'
		elif obj[8]<=1.0:
			# {"feature": "Age", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[3]<=3:
				# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[5]<=10:
					return 'False'
				elif obj[5]>10:
					return 'True'
				else: return 'True'
			elif obj[3]>3:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'True'
