def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[2]>1:
		# {"feature": "Coffeehouse", "instances": 28, "metric_value": 0.9059, "depth": 2}
		if obj[8]>0.0:
			# {"feature": "Time", "instances": 21, "metric_value": 0.7919, "depth": 3}
			if obj[1]<=1:
				# {"feature": "Education", "instances": 13, "metric_value": 0.9612, "depth": 4}
				if obj[5]<=2:
					# {"feature": "Gender", "instances": 10, "metric_value": 0.7219, "depth": 5}
					if obj[3]>0:
						return 'True'
					elif obj[3]<=0:
						# {"feature": "Occupation", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[6]>6:
							return 'True'
						elif obj[6]<=6:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[5]>2:
					return 'False'
				else: return 'False'
			elif obj[1]>1:
				return 'True'
			else: return 'True'
		elif obj[8]<=0.0:
			# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[9]>0.0:
				# {"feature": "Bar", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[7]>0.0:
					return 'False'
				elif obj[7]<=0.0:
					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]<=1:
						return 'True'
					elif obj[0]>1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[9]<=0.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[2]<=1:
		# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 2}
		if obj[1]<=3:
			return 'False'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	else: return 'False'
