def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9864, "depth": 1}
	if obj[2]>1:
		# {"feature": "Passanger", "instances": 37, "metric_value": 0.9953, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Education", "instances": 28, "metric_value": 0.9852, "depth": 3}
			if obj[5]>1:
				# {"feature": "Coffeehouse", "instances": 17, "metric_value": 0.7871, "depth": 4}
				if obj[8]<=2.0:
					# {"feature": "Bar", "instances": 12, "metric_value": 0.4138, "depth": 5}
					if obj[7]>0.0:
						return 'False'
					elif obj[7]<=0.0:
						# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[4]>2:
							return 'False'
						elif obj[4]<=2:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[8]>2.0:
					# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[6]<=5:
						return 'True'
					elif obj[6]>5:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[5]<=1:
				# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.8454, "depth": 4}
				if obj[8]<=1.0:
					# {"feature": "Time", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[1]<=2:
						# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[4]<=4:
							return 'True'
						elif obj[4]>4:
							return 'False'
						else: return 'False'
					elif obj[1]>2:
						return 'False'
					else: return 'False'
				elif obj[8]>1.0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[0]>2:
			# {"feature": "Time", "instances": 9, "metric_value": 0.5033, "depth": 3}
			if obj[1]<=3:
				return 'True'
			elif obj[1]>3:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[2]<=1:
		# {"feature": "Direction_same", "instances": 14, "metric_value": 0.5917, "depth": 2}
		if obj[10]<=0:
			return 'False'
		elif obj[10]>0:
			# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[0]<=1:
				return 'True'
			elif obj[0]>1:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
