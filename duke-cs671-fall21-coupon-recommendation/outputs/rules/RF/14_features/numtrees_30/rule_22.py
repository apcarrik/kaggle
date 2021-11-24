def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Age", "instances": 34, "metric_value": 0.874, "depth": 1}
	if obj[4]<=4:
		# {"feature": "Coupon", "instances": 28, "metric_value": 0.9403, "depth": 2}
		if obj[2]>1:
			# {"feature": "Income", "instances": 22, "metric_value": 0.8454, "depth": 3}
			if obj[8]<=5:
				# {"feature": "Bar", "instances": 14, "metric_value": 0.9852, "depth": 4}
				if obj[9]<=1.0:
					# {"feature": "Education", "instances": 9, "metric_value": 0.7642, "depth": 5}
					if obj[6]>1:
						return 'True'
					elif obj[6]<=1:
						# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[1]>0:
							# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[7]<=5:
								return 'True'
							elif obj[7]>5:
								return 'False'
							else: return 'False'
						elif obj[1]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[9]>1.0:
					# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[0]<=1:
						return 'False'
					elif obj[0]>1:
						# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[1]>2:
							return 'False'
						elif obj[1]<=2:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'False'
			elif obj[8]>5:
				return 'True'
			else: return 'True'
		elif obj[2]<=1:
			# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[1]>0:
				return 'False'
			elif obj[1]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[4]>4:
		return 'True'
	else: return 'True'
